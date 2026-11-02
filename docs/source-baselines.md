# Source baselines

This is a research inventory, not a claim that these sources are equivalent or mutually compatible. Verify versions and links before making implementation claims.

| Source | What it contributes | Caveat |
|---|---|---|
| [Agent Run Metrics Internet-Draft -02](https://datatracker.ietf.org/doc/draft-arsentev-agent-run-metrics/02/) | Draft discussion of agent run metrics/accounting | Individual Internet-Draft; not an IETF standard or endorsement. Draft status can change. |
| [OpenTelemetry GenAI metrics conventions](https://github.com/open-telemetry/semantic-conventions/blob/main/docs/gen-ai/gen-ai-metrics.md) | Observability metric conventions for GenAI | Semantic conventions evolve; pin a commit/version for any mapping claim. |
| [OpenTelemetry GenAI conventions](https://github.com/open-telemetry/semantic-conventions/tree/main/docs/gen-ai) | GenAI telemetry context, including traces | Telemetry semantics are not automatically billing/accounting semantics. |
| [FOCUS](https://focus.finops.org/) | Cloud financial management / cost data format | FOCUS is not an agent-run protocol or provider token-usage schema. |
| [OpenAI Agents SDK usage](https://openai.github.io/openai-agents-python/usage/) | SDK-specific usage reporting examples | SDK behavior is version-specific and provider/framework scoped. |
| [Docker Agent budgets](https://docs.docker.com/ai/docker-agent/configuration/budget) | Example of framework budget configuration | Budget enforcement is out of scope for OARMI. |

## Evidence policy

- A link alone does not establish interoperability.
- Record date/version/commit where practical.
- Do not label an individual draft as an RFC or standard.
- Do not assume the presence of a field means equivalent semantics across systems.
- Separate documented behavior from inferred behavior.
