"""Source-driven Decimal110 oracle. No candidate/module imports or execution.
Published TableA numbers independently transcribed from AHA Appendix4.
Freeze this output before JS candidate authorship/import/evaluation.
"""
from decimal import Decimal, localcontext
from pathlib import Path
from itertools import product
import json, hashlib, math, struct

ROOT = Path(__file__).resolve().parents[2]
DIR = ROOT/'reports/review-20261003/pce-2013-primary-source-final39'
sha = lambda b: hashlib.sha256(b).hexdigest()
models = {
 'female/nonHispanicWhite': {'age':'-29.799','age2':'4.884','tc':'13.540','ageTc':'-3.114','hdl':'-13.578','ageHdl':'3.149','sbpT':'2.019','sbpU':'1.957','smoke':'7.574','ageSmoke':'-1.665','diabetes':'0.661','mean':'-29.18','s0':'0.9665'},
 'female/nonHispanicAfricanAmerican': {'age':'17.114','tc':'0.940','hdl':'-18.920','ageHdl':'4.475','sbpT':'29.291','ageSbpT':'-6.432','sbpU':'27.820','ageSbpU':'-6.087','smoke':'0.691','diabetes':'0.874','mean':'86.61','s0':'0.9533'},
 'male/nonHispanicWhite': {'age':'12.344','tc':'11.853','ageTc':'-2.664','hdl':'-7.990','ageHdl':'1.769','sbpT':'1.797','sbpU':'1.764','smoke':'7.837','ageSmoke':'-1.795','diabetes':'0.658','mean':'61.18','s0':'0.9144'},
 'male/nonHispanicAfricanAmerican': {'age':'2.469','tc':'0.302','hdl':'-0.307','sbpT':'1.916','sbpU':'1.809','smoke':'0.549','diabetes':'0.645','mean':'19.54','s0':'0.8954'}
}
def own_expected(x):
    with localcontext() as ctx:
        ctx.prec = 110
        c={k:Decimal(v) for k,v in models[x['sex']+'/'+x['population']].items()}
        # Decimal(str(input)) is the explicit input-decimal identity. All sampled
        # lab/date values are integers or finite canonical decimal quantities.
        a=Decimal(str(x['ageYears'])).ln()
        t=Decimal(str(x['totalCholesterolMgDl'])).ln()
        h=Decimal(str(x['hdlCholesterolMgDl'])).ln()
        b=Decimal(str(x['systolicBpMmHg'])).ln()
        sm=Decimal(int(x['smoker'])); dm=Decimal(int(x['diabetes']))
        feature={'age':a,'age2':a*a,'tc':t,'ageTc':a*t,'hdl':h,'ageHdl':a*h,'smoke':sm,'ageSmoke':a*sm,'diabetes':dm}
        feature['sbpT' if x['treatedBp'] else 'sbpU']=b
        feature['ageSbpT' if x['treatedBp'] else 'ageSbpU']=a*b
        terms=[{'name':k,'coefficient':str(v),'feature':str(feature.get(k,Decimal(0))),'product':str(v*feature.get(k,Decimal(0)))} for k,v in c.items() if k not in ('mean','s0')]
        lp=sum((Decimal(z['product']) for z in terms),Decimal(0))
        centered=lp-c['mean']; hazard=centered.exp(); log_s=c['s0'].ln()*hazard
        prob=1-log_s.exp()
        return {'terms':terms,'linearPredictor':str(lp),'sumAbsoluteTerms':str(sum((abs(Decimal(z['product'])) for z in terms),Decimal(0))),'meanPredictorSum':str(c['mean']),'baselineSurvival':str(c['s0']),'centeredPredictor':str(centered),'relativeHazard':str(hazard),'survivalLog':str(log_s),'tenYearProbability':str(prob),'tenYearPercent':str(prob*100)}

rows=[]; seen=set()
def add(x, kind, published=None):
    identity=json.dumps(x,sort_keys=True,separators=(',',':'))
    if identity in seen: return
    seen.add(identity)
    rows.append({'id':f'pce-own-{len(rows)+1:05d}','kind':kind,'input':x,'expectedDecimal110':own_expected(x),**({'publishedRoundedPercent':published} if published is not None else {})})
for sex,pop in product(('female','male'),('nonHispanicWhite','nonHispanicAfricanAmerican')):
    published={('female','nonHispanicWhite'):'2.1',('female','nonHispanicAfricanAmerican'):'3.0',('male','nonHispanicWhite'):'5.3',('male','nonHispanicAfricanAmerican'):'6.1'}[sex,pop]
    add({'sex':sex,'population':pop,'ageYears':55,'totalCholesterolMgDl':213,'hdlCholesterolMgDl':50,'systolicBpMmHg':120,'treatedBp':False,'smoker':False,'diabetes':False},'published-rounded-tableA-profile',published)
    for age,tc,hdl,sbp,treated,smoker,diabetes in product((40,55,79),(130,213,320),(20,50,100),(90,120,200),(False,True),(False,True),(False,True)):
        add({'sex':sex,'population':pop,'ageYears':age,'totalCholesterolMgDl':tc,'hdlCholesterolMgDl':hdl,'systolicBpMmHg':sbp,'treatedBp':treated,'smoker':smoker,'diabetes':diabetes},'finite-in-domain-factorial')
    # Explicit fractional covariate witnesses (not exhaustive continuous domain).
    for n in range(24):
        add({'sex':sex,'population':pop,'ageYears':40+(n*157%3900)/100,'totalCholesterolMgDl':130+(n*719%19000)/100,'hdlCholesterolMgDl':20+(n*277%8000)/100,'systolicBpMmHg':90+(n*433%11000)/100,'treatedBp':bool(n%2),'smoker':bool((n//2)%2),'diabetes':bool((n//4)%2)},'deterministic-fractional-covariates')

coefficient_bytes=(json.dumps({'edition':'PCE2013-published-TableA-precision','models':models},ensure_ascii=False,indent=2)+'\n').encode()
coefficient_file=DIR/'published-coefficients.json'
coefficient_file.write_bytes(coefficient_bytes) if not coefficient_file.exists() else None
assert coefficient_file.read_bytes()==coefficient_bytes
sourcefile=DIR/'source-review.json'
bindings=[{'file':str(p.relative_to(ROOT)).replace('\\','/'),'sha256':sha(p.read_bytes())} for p in (sourcefile,coefficient_file,Path(__file__))]
result={'schema':'pre-import-independent-decimal-oracle-v1','model':'PCE2013-published-TableA-precision','generatedWithoutCandidateImports':True,'candidateDidNotExistAtGeneration':not(ROOT/'reports/review-20261003/pce-2013-numeric-candidate-final39.js').exists(),'decimalPrecision':110,'sources':bindings,'numericPolicyDeclaredBeforeCandidateImports':{'linearPredictor':'12EPS*sum(abs(Decimal source terms))','centeredPredictor':'12EPS*(sumAbsTerms+abs(mean))','probability':'centeredBound * (-ln(S0)) * exp(centered) * exp(ln(S0)*exp(centered)) + 24EPS*abs(probability)','percent':'100*probabilityBound + 2EPS*abs(percent)','existingFixtureTolerancesChanged':False},'sourcePrecisionPolicy':'literal published rounded coefficients/means/S0; no unknown higher precision or paper intermediate rounding substituted','inputIdentity':'canonical JSON sorted keys per input within historical model; Decimal(str(number))','coverage':{'scenarios':len(rows),'uniqueInputs':len(seen),'models':4,'publishedProfiles':4,'continuousExhaustive':False},'rows':rows,'approvals':{'clinical':'not-performed','rights':'not-performed','professionalLanguage':'not-performed','fullMethod':'not-performed'}}
outfile=ROOT/'reports/review-20261003/pce-2013-own-decimal-expectations-final39.json'
encoded=(json.dumps(result,ensure_ascii=False,indent=2)+'\n').encode()
with outfile.open('xb') as f: f.write(encoded)
print(json.dumps({'file':str(outfile.relative_to(ROOT)),'sha256':sha(encoded),'bytes':len(encoded),'rows':len(rows),'candidateDidNotExistAtGeneration':result['candidateDidNotExistAtGeneration'],'publishedRoundedChecks':[{ 'model':r['input']['sex']+'/'+r['input']['population'],'decimalPercent':r['expectedDecimal110']['tenYearPercent'],'publishedRoundedPercent':r['publishedRoundedPercent'],'matchesOneDecimal':Decimal(r['expectedDecimal110']['tenYearPercent']).quantize(Decimal('.1'))==Decimal(r['publishedRoundedPercent'])} for r in rows if 'publishedRoundedPercent'in r]},ensure_ascii=False))
