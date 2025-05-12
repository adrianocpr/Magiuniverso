# Fluxo de Atualização IA via GitHub Actions

## Como funciona

Este sistema roda periodicamente ou manualmente para sugerir melhorias no código com base em simulações de uma IA.

### Requisitos

- Token do GitHub com permissões `repo` e `workflow`.
- Adicione no Render como variável de ambiente: `GH_TOKEN`.
- Crie o repositório no GitHub e suba este conteúdo.

### Resultado Esperado

O GitHub Actions irá abrir Pull Requests com melhorias automáticas ou sugestões.

---
Você pode integrar com GPTs reais usando o script `ai_patch_generator.py`.