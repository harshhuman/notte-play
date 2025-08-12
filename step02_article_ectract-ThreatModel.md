# Step 02 — Page Extract (OWASP GenAI) — Threat Model

## 1. Description
This program uses a **Notte browser agent** to visit [https://genai.owasp.org](https://genai.owasp.org) and extract structured metadata (`title`, `intro`, and key internal links).  
The agent runs under strict constraints:
- Same-domain navigation (`genai.owasp.org`)
- No forms, no downloads
- Max 5 steps
- Schema-locked JSON output
- Read-only navigation, no tool execution

---

## 2. Asset Inventory

| Asset                    | Description                                                                | Classification       |
|--------------------------|----------------------------------------------------------------------------|----------------------|
| API Keys                 | `OPENAI_API_KEY` loaded from `.env`.                                       | Secret               |
| Agent Configuration      | Task prompt, model selection (`openai/gpt-4o-mini`), `max_steps=5`, domain allow-list. | Internal config      |
| Local Filesystem         | Python environment, `.env` file, console output.                           | Sensitive if secrets |
| Browser Session          | Live browser connection to `genai.owasp.org`.                              | Public               |
| Model Responses          | JSON output containing extracted page metadata.                            | Internal             |

---

## 3. Threat Model Table

| TID  | Threat Name                              | Threat Description                                                                                                                                                                                                                                                                                      | Current Mitigations                                                                                                                                                                                                                                        | Recommended Additional Mitigations                                                                                                                                                                                                                                   |
|------|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| T6   | Intent Breaking & Goal Manipulation      | Attackers could attempt to alter the agent’s intended extraction goals by injecting malicious instructions into the OWASP GenAI homepage content (e.g., telling the agent to navigate elsewhere, exfiltrate data, or change output schema).                                                              | - Domain allow-list restricts navigation to `genai.owasp.org`<br>- JSON schema fixed in prompt<br>- `max_steps=5` limit<br>- No tools beyond read-only navigation                                                                                           | - Add automated prompt injection detection tests<br>- Implement secondary model for output validation                                                                                                                                                              |
| T7   | Misaligned & Deceptive Behaviors         | Agent might generate output that appears valid but omits or alters data due to deceptive content or adversarial HTML manipulation.                                                                                                                                                                     | - Fixed schema for keys/values<br>- Manual review of output<br>- No downstream automation                                                                                                                                                                 | - Integrate automated output diffing against known-good baseline<br>- Deploy behavioral consistency checks                                                                                                                                                          |
| T5   | Cascading Hallucination Attacks          | If agent misinterprets content and stores it in persistent memory, errors could propagate across runs or contaminate other tasks. While Step 02 has no persistent memory, a future extension could introduce this risk.                                                                                 | - No persistent memory<br>- Single-run context only<br>- Task prompt limits scope                                                                                                                                                                         | - If persistent memory is added, enforce memory content validation<br>- Add rollback capability for memory state                                                                                                                                                    |
| T2   | Tool Misuse                              | If extended with tool actions (e.g., file downloads, API posts), injected instructions could misuse them.                                                                                                                                                                                                | - No form submissions or downloads<br>- Only read/goto actions allowed                                                                                                                                                                                    | - Apply strict tool invocation policies before enabling tools<br>- Require explicit human approval for risky actions                                                                                                                                                |
| T4   | Resource Overload                        | Maliciously crafted content (e.g., huge DOM, infinite scroll) could cause excessive processing, token use, or degraded performance.                                                                                                                                                                     | - `max_steps=5` limits traversal<br>- Read-only scope prevents chasing endless loops                                                                                                                                                                      | - Add DOM size checks before extraction<br>- Monitor and alert on abnormal token usage per run                                                                                                                                                                      |
| T9   | Identity Spoofing & Impersonation        | If environment variables were exposed in context, attacker-controlled content could trick the agent into revealing secrets or impersonating a user.                                                                                                                                                      | - Environment variables never printed or injected into prompts<br>- No vault credentials used<br>- Prompt content strictly controlled                                                                                                                     | - Scan prompt construction pipeline for unintended variable interpolation<br>- Apply runtime guardrails to block sensitive strings in output                                                                                                                         |

---

## 4. Residual Risks
- A full compromise of `genai.owasp.org` could inject malicious instructions or misleading content that bypass schema constraints.
- Manual review of outputs is still required; no automated anomaly detection for subtle deception.
- Resource exhaustion from complex DOM structures is limited but not fully prevented without DOM size checks.

---

## 5. References
- [OWASP Agentic AI Threat Taxonomy (TIDs)](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- *Agentic AI — Threats and Mitigations*, Feb 2025, OWASP Agentic Security Initiative
