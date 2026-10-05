# PCE2013 · modelo histórico

Reproduz a equação histórica de 2013 para o primeiro infarto não fatal, morte coronária ou AVC fatal/não fatal em dez anos. Não estima insuficiência cardíaca, risco vitalício ou efeito de tratamento.

## Método e edição

PCE2013 · coeficientes publicados no Apêndice 4, Tabelas A/B; modelo histórico

## Entradas

- **Sexo na equação publicada** (`sex`, `sel`)
  - `female`: Feminino
  - `male`: Masculino
- **Grupo da população de derivação** (`population`, `sel`)
  - `nonHispanicWhite`: Pessoa branca não hispânica
  - `nonHispanicAfricanAmerican`: Pessoa afro-americana não hispânica
  - `unsupported`: Outro grupo / não determinado
- **Idade** (`ageYears`, `num`) — anos [40–79]
- **Colesterol total** (`totalCholesterolMgDl`, `num`) — mg/dL [130–320]
- **Colesterol HDL** (`hdlCholesterolMgDl`, `num`) — mg/dL [20–100]
- **Pressão arterial sistólica** (`systolicBpMmHg`, `num`) — mmHg [90–200]
- **Tratamento anti-hipertensivo atual?** (`treatedBp`, `sel`)
  - `yes`: Sim
  - `no`: Não
- **Tabagismo atual?** (`smoker`, `sel`)
  - `yes`: Sim
  - `no`: Não
- **Diabetes?** (`diabetes`, `sel`)
  - `yes`: Sim
  - `no`: Não
- **Infarto do miocárdio prévio?** (`priorMI`, `sel`)
  - `yes`: Sim
  - `no`: Não
  - `unknown`: Desconhecido
- **AVC prévio?** (`priorStroke`, `sel`)
  - `yes`: Sim
  - `no`: Não
  - `unknown`: Desconhecido
- **Insuficiência cardíaca prévia?** (`priorHF`, `sel`)
  - `yes`: Sim
  - `no`: Não
  - `unknown`: Desconhecido
- **Intervenção coronária percutânea prévia?** (`priorPCI`, `sel`)
  - `yes`: Sim
  - `no`: Não
  - `unknown`: Desconhecido
- **Cirurgia de revascularização miocárdica prévia?** (`priorCABG`, `sel`)
  - `yes`: Sim
  - `no`: Não
  - `unknown`: Desconhecido
- **Fibrilação atrial prévia?** (`atrialFibrillation`, `sel`)
  - `yes`: Sim
  - `no`: Não
  - `unknown`: Desconhecido
- **Condição aparentemente saudável na avaliação basal confirmada?** (`apparentlyHealthy`, `sel`)
  - `yes`: Sim
  - `no`: Não
  - `unknown`: Desconhecido
- **Uso do modelo histórico para pesquisa confirmado?** (`historicalResearchConfirmed`, `sel`)
  - `yes`: Sim
  - `no`: Não
  - `unknown`: Desconhecido

## Limites e revisão

As categorias populacionais são as duas categorias históricas dos EUA da fonte; não substituir silenciosamente outros grupos. Idade: 40–79 anos; colesterol total: 130–320 mg/dL; HDL: 20–100 mg/dL; pressão sistólica: 90–200 mmHg. Os três limites laboratoriais/pressóricos são convenções do estimador oficial legado. Responda explicitamente aos antecedentes e às confirmações; resposta desconhecida ou exclusão não produz estimativa. O ACC informa que o risco em dez anos calculado pela PCE não é mais apoiado pela política clínica/diretrizes atuais. Esta implementação é candidata de pesquisa histórica, não PREVENT, recomendação terapêutica ou validação clínica. Um exemplo publicado para homem branco permanece divergente: a equação com os coeficientes publicados arredonda para 5,4%, enquanto a tabela imprime 5,3%. Não se alteraram coeficientes para esconder a diferença. Permissões de distribuição e revisão clínica/profissional não realizadas.

O ACC informa que o risco em dez anos calculado pela PCE não é mais apoiado pela política clínica/diretrizes atuais. Esta implementação é candidata de pesquisa histórica, não PREVENT, recomendação terapêutica ou validação clínica. Um exemplo publicado para homem branco permanece divergente: a equação com os coeficientes publicados arredonda para 5,4%, enquanto a tabela imprime 5,3%. Não se alteraram coeficientes para esconder a diferença. Permissões de distribuição e revisão clínica/profissional não realizadas.

Conferência técnica com dados sintéticos. Revisão clínica independente e revisão profissional das traduções não foram realizadas.

## Executar com dados sintéticos

```sh
node cli.cjs examples/input.json pt-BR
```

## Resultados

- Estimativa histórica em 10 anos (%)
<p>Probabilidade em 10 anos = 1 − S₀<sup>exp(ΣβX − média)</sup>; resultado percentual = 100 × probabilidade. X usa logaritmos naturais e interações da coluna populacional/sexo publicada. Mantém a precisão publicada dos coeficientes; a apresentação de uma casa decimal não altera o resultado bruto.</p>

## Fonte e direitos

- https://doi.org/10.1161/01.cir.0000437741.48606.98
- https://www.heart.org/-/media/Data-Import/downloadables/0/D/A/2013-AHA-ACC-Cardiovascular-Risk-Guidelines-UCM_464291.pdf
- https://tools.acc.org/cvd-risk-estimator-plus/

[RIGHTS-SCOPE.md](../RIGHTS-SCOPE.md) · [test receipts](../evidence/)
