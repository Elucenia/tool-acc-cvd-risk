'use strict';
const core=require('./pce2013-core.js');
const ui=require('./pce2013-interface.cjs');
const definition=ui.definition('pt-BR');
const metadata=Object.freeze({id:definition.id,title:definition.title,fields:definition.fields,methodVersion:definition.methodVersion,reviewStatus:'needs-review',clinicalValidation:'not-performed'});
const keys=definition.fields.map(f=>f[0]);
const fail=(code,field)=>({error:code==='METHOD_SCOPE'?'Os dados ou o contexto não correspondem ao escopo histórico documentado.':'Confira o campo e seu tipo documentado.',code,...(field?{field}:{})});
function calculate(input){
 if(!input||typeof input!=='object'||Array.isArray(input))return fail('INVALID_INPUT');
 for(const k of Reflect.ownKeys(input)){if(typeof k!=='string'||!keys.includes(k))return fail('UNKNOWN_FIELD');const d=Object.getOwnPropertyDescriptor(input,k);if(!d||!Object.hasOwn(d,'value'))return fail('INVALID_INPUT',k);}
 for(const [name,,kind,opt]of metadata.fields){if(!Object.hasOwn(input,name))return fail('REQUIRED_FIELD',name);const value=input[name];if(value===undefined||value===null||value==='')return fail('REQUIRED_FIELD',name);if(kind==='num'){if(typeof value!=='number'||!Number.isFinite(value))return fail('INVALID_INPUT',name);if(value<opt.min||value>opt.max)return fail('OUT_OF_RANGE',name);}else if(typeof value!=='string'||!Object.hasOwn(opt.opts,value))return fail('INVALID_OPTION',name);}
 if(input.population==='unsupported')return fail('METHOD_SCOPE','population');
 for(const name of ui.historyKeys)if(input[name]!=='no')return fail('METHOD_SCOPE',name);
 for(const name of ['apparentlyHealthy','historicalResearchConfirmed'])if(input[name]!=='yes')return fail('METHOD_SCOPE',name);
 const numeric=Object.fromEntries(core.inputKeys.map(name=>[name,['treatedBp','smoker','diabetes'].includes(name)?input[name]==='yes':input[name]]));
 const result=core.calculate(numeric);
 return {label:ui.copy['pt-BR'].result,main:[result.raw.tenYearPercent.toFixed(1).replace('.',','),'%'],raw:{...result.raw},modelKey:result.modelKey,horizonYears:10};
}
module.exports=Object.freeze({metadata,calculate});
