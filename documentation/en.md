# PCE2013 · historical model

Reproduces the historical 2013 equation for first nonfatal myocardial infarction, coronary death or fatal/nonfatal stroke over ten years. It does not estimate heart failure, lifetime risk or treatment effects.

## Method and edition

PCE2013 · published Appendix 4, Tables A/B coefficients; historical model

## Inputs

- **Sex in the published equation** (`sex`, `sel`)
  - `female`: Female
  - `male`: Male
- **Derivation population group** (`population`, `sel`)
  - `nonHispanicWhite`: Non-Hispanic White person
  - `nonHispanicAfricanAmerican`: Non-Hispanic African-American person
  - `unsupported`: Other group / not determined
- **Age** (`ageYears`, `num`) — years [40–79]
- **Total cholesterol** (`totalCholesterolMgDl`, `num`) — mg/dL [130–320]
- **HDL cholesterol** (`hdlCholesterolMgDl`, `num`) — mg/dL [20–100]
- **Systolic blood pressure** (`systolicBpMmHg`, `num`) — mmHg [90–200]
- **Current antihypertensive treatment?** (`treatedBp`, `sel`)
  - `yes`: Yes
  - `no`: No
- **Current smoking?** (`smoker`, `sel`)
  - `yes`: Yes
  - `no`: No
- **Diabetes?** (`diabetes`, `sel`)
  - `yes`: Yes
  - `no`: No
- **Previous myocardial infarction?** (`priorMI`, `sel`)
  - `yes`: Yes
  - `no`: No
  - `unknown`: Unknown
- **Previous stroke?** (`priorStroke`, `sel`)
  - `yes`: Yes
  - `no`: No
  - `unknown`: Unknown
- **Previous heart failure?** (`priorHF`, `sel`)
  - `yes`: Yes
  - `no`: No
  - `unknown`: Unknown
- **Previous percutaneous coronary intervention?** (`priorPCI`, `sel`)
  - `yes`: Yes
  - `no`: No
  - `unknown`: Unknown
- **Previous coronary artery bypass surgery?** (`priorCABG`, `sel`)
  - `yes`: Yes
  - `no`: No
  - `unknown`: Unknown
- **Previous atrial fibrillation?** (`atrialFibrillation`, `sel`)
  - `yes`: Yes
  - `no`: No
  - `unknown`: Unknown
- **Apparently healthy status at baseline assessment confirmed?** (`apparentlyHealthy`, `sel`)
  - `yes`: Yes
  - `no`: No
  - `unknown`: Unknown
- **Use of the historical model for research confirmed?** (`historicalResearchConfirmed`, `sel`)
  - `yes`: Yes
  - `no`: No
  - `unknown`: Unknown

## Limits and review

Population categories are the source’s two historical US categories; do not silently substitute other groups. Age: 40–79 years; total cholesterol: 130–320 mg/dL; HDL: 20–100 mg/dL; systolic pressure: 90–200 mmHg. The three laboratory/pressure limits are legacy official-estimator conventions. Answer history and confirmation fields explicitly; unknown answers or exclusions do not produce an estimate. ACC states that PCE-derived ten-year risk is no longer supported by current clinical policy/guidelines. This is a historical research candidate, not PREVENT, treatment advice or clinical validation. One published White-male example remains discrepant: the equation using published coefficients rounds to 5.4%, while the table prints 5.3%. Coefficients were not changed to hide the difference. Distribution permission has not been obtained; clinical/professional review has not been performed.

ACC states that PCE-derived ten-year risk is no longer supported by current clinical policy/guidelines. This is a historical research candidate, not PREVENT, treatment advice or clinical validation. One published White-male example remains discrepant: the equation using published coefficients rounds to 5.4%, while the table prints 5.3%. Coefficients were not changed to hide the difference. Distribution permission has not been obtained; clinical/professional review has not been performed.

Technical checks use synthetic data. Independent clinical review and professional translation review have not been performed.

## Run with synthetic data

```sh
node cli.cjs examples/input.json en
```

## Results

- Historical 10-year estimate (%)
<p>10-year probability = 1 − S₀<sup>exp(ΣβX − mean)</sup>; percentage = 100 × probability. X uses natural logarithms and interactions from the published population/sex column. Published coefficient precision is retained; one-decimal presentation does not change the raw result.</p>

## Source and rights

- https://doi.org/10.1161/01.cir.0000437741.48606.98
- https://www.heart.org/-/media/Data-Import/downloadables/0/D/A/2013-AHA-ACC-Cardiovascular-Risk-Guidelines-UCM_464291.pdf
- https://tools.acc.org/cvd-risk-estimator-plus/

[RIGHTS-SCOPE.md](../RIGHTS-SCOPE.md) · [test receipts](../evidence/)
