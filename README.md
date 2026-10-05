# PCE2013 historical research implementation

Original ELUCENIA implementation of the four published 2013 pooled-cohort equations. It estimates the first hard ASCVD event over ten years using the published rounded coefficient precision. It is not PREVENT, current treatment guidance, lifetime/optimal risk, or the complete ACC provider.

## Run

`node test.cjs` checks the independently authored Decimal110 mathematical corpus,20 explicit root fixtures and documented refusals. `calculator.js` requires `pce2013-core.js` and `pce2013-interface.cjs`. Inputs and cases are synthetic. No personal identifiers are accepted. Lipids use mg/dL; pressure mmHg; age years. An SI conversion is not inferred.

## Sources and limits

Goff et al. DOI10.1161/01.cir.0000437741.48606.98. [AHA author manuscript, Appendix4 TablesA/B](https://www.heart.org/-/media/Data-Import/downloadables/0/D/A/2013-AHA-ACC-Cardiovascular-Risk-Guidelines-UCM_464291.pdf). [Current ACC model policy](https://tools.acc.org/cvd-risk-estimator-plus/). ACC now states the PCE risk magnitude is no longer supported by current clinical policy/guidelines.

Four historical US sex/population groups only; other groups are rejected, not silently substituted. All17 answers must be explicit. Prior cardiovascular disease, unknown histories or missing historical-research confirmation produce no estimate. A White-male published example prints5.3%; the published coefficients yield5.4% after one-decimal rounding. This discrepancy is preserved in limits and evidence.

Clinical review and professional translation review have not been performed. Third-party article/provider assets and the provider interface/code are not distributed. This original source implementation is not an authorization to redistribute third-party materials.
