/*
 * Independently authored numerical research core from Goff et al., PCE2013
 * published Appendix4 TableA/TableB, DOI10.1161/01.cir.0000437741.48606.98.
 * The published (rounded) coefficient precision is the explicit edition.
 * This is not ACC/AHA provider code, a current clinical recommendation or a
 * licensed clinical product. Article/provider redistribution is not approved.
 * No eligibility, treatment, lifetime, PREVENT or unmodeled-population mapping.
 */
(function(root,factory){
  if(typeof module==='object'&&module.exports)module.exports=factory();
  else root.EluceniaPce2013ResearchCandidate=factory();
})(typeof globalThis!=='undefined'?globalThis:this,function(){
  'use strict';
  const EDITION='PCE2013-published-TableA-precision';
  const KEYS=Object.freeze(['sex','population','ageYears','totalCholesterolMgDl','hdlCholesterolMgDl','systolicBpMmHg','treatedBp','smoker','diabetes']);
  const MODEL=Object.freeze({
    'female/nonHispanicWhite':Object.freeze({age:-29.799,age2:4.884,tc:13.540,ageTc:-3.114,hdl:-13.578,ageHdl:3.149,sbpT:2.019,sbpU:1.957,smoke:7.574,ageSmoke:-1.665,diabetes:0.661,mean:-29.18,s0:.9665}),
    'female/nonHispanicAfricanAmerican':Object.freeze({age:17.114,tc:.940,hdl:-18.920,ageHdl:4.475,sbpT:29.291,ageSbpT:-6.432,sbpU:27.820,ageSbpU:-6.087,smoke:.691,diabetes:.874,mean:86.61,s0:.9533}),
    'male/nonHispanicWhite':Object.freeze({age:12.344,tc:11.853,ageTc:-2.664,hdl:-7.990,ageHdl:1.769,sbpT:1.797,sbpU:1.764,smoke:7.837,ageSmoke:-1.795,diabetes:.658,mean:61.18,s0:.9144}),
    'male/nonHispanicAfricanAmerican':Object.freeze({age:2.469,tc:.302,hdl:-.307,sbpT:1.916,sbpU:1.809,smoke:.549,diabetes:.645,mean:19.54,s0:.8954})
  });
  const SCOPE='Historical numerical research only; first hard ASCVD probability over10years at published coefficient precision. Clinical eligibility, current guidance and provider/licensing approval are not established.';
  function invalid(field){return{error:{code:'INVALID_RESEARCH_INPUT',field},edition:EDITION,scope:SCOPE};}
  function finiteRange(value,min,max){return typeof value==='number'&&Number.isFinite(value)&&value>=min&&value<=max;}
  function sum(values){let s=0,correction=0;for(const v of values){const next=s+v;correction+=Math.abs(s)>=Math.abs(v)?(s-next)+v:(v-next)+s;s=next;}return s+correction;}
  function calculate(x){
    if(!x||Object.prototype.toString.call(x)!=='[object Object]')return invalid('input');
    const supplied=Reflect.ownKeys(x);
    if(supplied.length!==KEYS.length||supplied.some(k=>typeof k!=='string'||!KEYS.includes(k)))return invalid('inputKeys');
    if(KEYS.some(k=>!Object.prototype.hasOwnProperty.call(x,k)||!Object.prototype.hasOwnProperty.call(Object.getOwnPropertyDescriptor(x,k),'value')))return invalid('inputKeys');
    if(!['female','male'].includes(x.sex))return invalid('sex');
    if(!['nonHispanicWhite','nonHispanicAfricanAmerican'].includes(x.population))return invalid('population');
    for(const [k,min,max] of [['ageYears',40,79],['totalCholesterolMgDl',130,320],['hdlCholesterolMgDl',20,100],['systolicBpMmHg',90,200]])if(!finiteRange(x[k],min,max))return invalid(k);
    for(const k of ['treatedBp','smoker','diabetes'])if(typeof x[k]!=='boolean')return invalid(k);
    const modelKey=x.sex+'/'+x.population,c=MODEL[modelKey];
    const a=Math.log(x.ageYears),tc=Math.log(x.totalCholesterolMgDl),hdl=Math.log(x.hdlCholesterolMgDl),sbp=Math.log(x.systolicBpMmHg),smoker=Number(x.smoker),diabetes=Number(x.diabetes);
    const f={age:a,age2:a*a,tc,ageTc:a*tc,hdl,ageHdl:a*hdl,smoke:smoker,ageSmoke:a*smoker,diabetes};
    f[x.treatedBp?'sbpT':'sbpU']=sbp;
    f[x.treatedBp?'ageSbpT':'ageSbpU']=a*sbp;
    const terms=Object.entries(c).filter(([name])=>name!=='mean'&&name!=='s0').map(([name,coefficient])=>({name,coefficient,feature:f[name]??0,product:coefficient*(f[name]??0)}));
    const linearPredictor=sum(terms.map(t=>t.product)),centeredPredictor=linearPredictor-c.mean,relativeHazard=Math.exp(centeredPredictor),survivalLog=Math.log(c.s0)*relativeHazard;
    // -expm1(log(S0)*exp(LP-mean)) is algebraically the published survival
    // transformation. It retains small probabilities without 1-exp cancellation.
    const tenYearProbability=-Math.expm1(survivalLog),tenYearPercent=100*tenYearProbability;
    return{model:EDITION,edition:EDITION,horizonYears:10,modelKey,raw:{linearPredictor,meanPredictorSum:c.mean,baselineSurvival:c.s0,centeredPredictor,relativeHazard,survivalLog,tenYearProbability,tenYearPercent,terms},scope:SCOPE};
  }
  return Object.freeze({calculate,edition:EDITION,inputKeys:KEYS});
});
