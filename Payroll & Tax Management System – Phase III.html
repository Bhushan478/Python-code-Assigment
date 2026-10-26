<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Payroll & Tax Management System</title>
<style>
:root{box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px);--bg:#f5f7fa;--card:#fff;--tx:#1b2430;--mu:#5d6b7c;--bd:#d9e0e8;--ac:#1f4fa3;--ok:#1a7f4b;--er:#c0392b}
@media(prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#10151c;--card:#19212b;--tx:#e8edf3;--mu:#9aa8b8;--bd:#2c3846;--ac:#6ea0f5;--ok:#4fcf8f;--er:#ff7b6b}}
:root[data-theme="dark"]{--bg:#10151c;--card:#19212b;--tx:#e8edf3;--mu:#9aa8b8;--bd:#2c3846;--ac:#6ea0f5;--ok:#4fcf8f;--er:#ff7b6b}
html{scroll-padding-top:env(safe-area-inset-top,0px)}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--tx);font:15px/1.5 system-ui,-apple-system,Segoe UI,Roboto,sans-serif}
header{padding:16px 20px;border-bottom:1px solid var(--bd);background:var(--card)}
h1{font-size:19px;margin:0}header p{margin:2px 0 0;color:var(--mu);font-size:13px}
nav{display:flex;gap:6px;padding:10px 20px;flex-wrap:wrap}
nav button,.btn{border:1px solid var(--bd);background:var(--card);color:var(--tx);padding:7px 14px;border-radius:8px;cursor:pointer;font:inherit}
nav button.on,.btn.p{background:var(--ac);color:#fff;border-color:var(--ac)}
.btn.d{color:var(--er)}.btn.s{padding:3px 9px;font-size:13px}
main{padding:0 20px 30px;max-width:980px;margin:auto}
.card{background:var(--card);border:1px solid var(--bd);border-radius:12px;padding:16px;margin-bottom:14px}
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px}
.stat b{display:block;font-size:20px}.stat span{color:var(--mu);font-size:12px}
.tw{overflow-x:auto}table{width:100%;border-collapse:collapse;min-width:560px}
th,td{padding:8px;border-bottom:1px solid var(--bd);text-align:left}th{color:var(--mu);font-size:12px;text-transform:uppercase}
td.n,th.n{text-align:right}
.form{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:12px}
label{display:block;font-size:12px;color:var(--mu);margin-bottom:3px}
input,select{width:100%;padding:8px;border:1px solid var(--bd);border-radius:8px;background:var(--bg);color:var(--tx);font:inherit}
.msg{padding:8px 12px;border-radius:8px;margin:10px 0;font-size:14px}.msg.ok{color:var(--ok);border:1px solid var(--ok)}.msg.er{color:var(--er);border:1px solid var(--er)}
.slip dl{display:grid;grid-template-columns:1fr auto;gap:4px 16px;margin:0}.slip dt{color:var(--mu)}.slip dd{margin:0;text-align:right}
.slip .net{font-weight:700;font-size:17px;border-top:2px solid var(--tx);padding-top:6px}
.t-ok{color:var(--ok)}.t-er{color:var(--er)}
@media print{header,nav,.noprint{display:none!important}}
</style></head><body>
<header><h1>Advanced Employee Payroll &amp; Tax Management System</h1>
<p>Phase III · Python Programming (N-PCCCM304P) · Bhushan Marbate [CM25074]</p></header>
<nav id="nav"></nav>
<main id="app"></main>
<script>
/* ===== Business logic (OOP port of the Phase II Python code) ===== */
const TAX_SLABS=[[25000,0],[50000,.05],[100000,.10],[Infinity,.20]];
const PF_RATE=.12, PROF_TAX=200, PROF_TAX_LIMIT=15000;
class Employee{
  constructor(id,name,basic,allowances,performance){
    this.id=id;this.name=name;this.basic=basic;this.allowances=allowances;this.performance=performance}
}
class PayrollError extends Error{}
class Payroll{
  static tax(gross){let t=0,prev=0;for(const[l,r]of TAX_SLABS){const a=Math.min(gross,l)-prev;if(a>0)t+=a*r;if(gross<=l)break;prev=l}return Math.round(t*100)/100}
  static bonus(basic,p){return p>=90?basic*.15:p>=75?basic*.10:p>=60?basic*.05:0}
  static salary(e){
    const bonus=Payroll.bonus(e.basic,e.performance),gross=e.basic+e.allowances+bonus,pf=e.basic*PF_RATE,
      pt=gross>PROF_TAX_LIMIT?PROF_TAX:0,it=Payroll.tax(gross),ded=pf+pt+it;
    return{bonus,gross,pf,pt,it,ded,net:gross-ded}}
  static validate(o,existing,editing){
    const id=String(o.id||"").trim().toUpperCase(),name=String(o.name||"").trim();
    if(!/^EMP\d{3,6}$/.test(id))throw new PayrollError("Employee ID must look like EMP1001.");
    if(!editing&&existing.has(id))throw new PayrollError("Employee ID "+id+" already exists.");
    if(name.length<2||!/^[A-Za-z .'-]+$/.test(name))throw new PayrollError("Enter a valid name (letters only).");
    const n=k=>{const v=Number(o[k]);if(o[k]===""||o[k]===null||!isFinite(v))throw new PayrollError(k+" must be a number.");return v};
    const basic=n("basic"),al=n("allowances"),p=n("performance");
    if(basic<=0)throw new PayrollError("Basic salary must be greater than 0.");
    if(al<0)throw new PayrollError("Allowances cannot be negative.");
    if(p<0||p>100)throw new PayrollError("Performance must be between 0 and 100.");
    return new Employee(id,name,basic,al,p)}
}
class Store{
  constructor(key){this.key=key;this.map=new Map();this.load()}
  load(){let raw=null;try{raw=localStorage.getItem(this.key)}catch(e){}
    try{const a=raw?JSON.parse(raw):null;if(Array.isArray(a)){a.forEach(o=>this.map.set(o.id,new Employee(o.id,o.name,o.basic,o.allowances,o.performance)));return}}catch(e){}
    this.seed()}
  seed(){[["EMP1001","Rahul Sharma",30000,8000,80],["EMP1002","Priya Deshmukh",40000,9000,92],["EMP1003","Aman Verma",26000,5000,65]]
    .forEach(a=>this.map.set(a[0],new Employee(...a)));this.save()}
  save(){try{localStorage.setItem(this.key,JSON.stringify([...this.map.values()]))}catch(e){}}
  all(){return[...this.map.values()]}
  add(e){this.map.set(e.id,e);this.save()}
  del(id){const r=this.map.delete(id);this.save();return r}
  reset(){this.map.clear();this.seed()}
}
/* ===== UI ===== */
const store=new Store("payroll_phase3_v1");
const $=s=>document.querySelector(s);
const esc=s=>String(s).replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
const inr=v=>"₹"+Number(v).toLocaleString("en-IN",{minimumFractionDigits:2,maximumFractionDigits:2});
const TABS=["Dashboard","Employees","Add / Edit","Salary Slip","Payroll Report","Tax Slabs","Self-Tests"];
let tab=0,edit=null,slipId=null,flash=null,q="";
function nav(){$("#nav").innerHTML=TABS.map((t,i)=>`<button class="${i===tab?"on":""}" data-t="${i}">${t}</button>`).join("")}
$("#nav").onclick=e=>{const t=e.target.dataset.t;if(t!==undefined){tab=+t;if(tab!==2)edit=null;flash=null;render()}};
function msg(){return flash?`<div class="msg ${flash.t}">${esc(flash.m)}</div>`:""}
function render(){nav();$("#app").innerHTML=[vDash,vEmp,vForm,vSlip,vRep,vTax,vTest][tab]();
  if(tab===2)$("#f").onsubmit=submit;}
function vDash(){const l=store.all().map(e=>({e,s:Payroll.salary(e)}));
  const sum=k=>l.reduce((a,x)=>a+x.s[k],0);
  const top=l.slice().sort((a,b)=>b.s.net-a.s.net)[0];
  return`<div class="stats" style="margin:6px 0 14px">
  <div class="card stat"><b>${l.length}</b><span>Employees</span></div>
  <div class="card stat"><b>${inr(sum("gross"))}</b><span>Total gross</span></div>
  <div class="card stat"><b>${inr(sum("ded"))}</b><span>Total deductions</span></div>
  <div class="card stat"><b>${inr(sum("net"))}</b><span>Total net payout</span></div></div>
  <div class="card"><b>Summary</b><p style="color:var(--mu);margin:6px 0 0">${top?`Highest net salary: ${esc(top.e.name)} (${inr(top.s.net)}). Total income tax: ${inr(sum("it"))}. Total PF: ${inr(sum("pf"))}.`:"No employees yet."} Data is saved in this browser automatically.</p></div>
  <button class="btn d" onclick="if(confirm('Reset to demo data?')){store.reset();flash={t:'ok',m:'Demo data restored.'};render()}">Reset demo data</button>${msg()}`}
function vEmp(){const l=store.all().filter(e=>(e.id+e.name).toLowerCase().includes(q.toLowerCase()));
  return`${msg()}<div class="card"><input id="q" placeholder="Search by ID or name…" value="${esc(q)}" oninput="q=this.value;render();const i=$('#q');i.focus();i.setSelectionRange(q.length,q.length)">
  <div class="tw" style="margin-top:10px"><table><tr><th>ID</th><th>Name</th><th class="n">Basic</th><th class="n">Perf</th><th class="n">Net</th><th></th></tr>
  ${l.map(e=>`<tr><td>${esc(e.id)}</td><td>${esc(e.name)}</td><td class="n">${inr(e.basic)}</td><td class="n">${e.performance}</td><td class="n">${inr(Payroll.salary(e).net)}</td>
  <td class="n"><button class="btn s" onclick="slipId='${esc(e.id)}';tab=3;render()">Slip</button> <button class="btn s" onclick="edit='${esc(e.id)}';tab=2;render()">Edit</button> <button class="btn s d" onclick="delE('${esc(e.id)}')">Delete</button></td></tr>`).join("")||`<tr><td colspan="6">No records found.</td></tr>`}
  </table></div></div>`}
function delE(id){if(confirm("Delete "+id+"?")){store.del(id);flash={t:"ok",m:"Employee record deleted successfully."};render()}}
function vForm(){const e=edit?store.map.get(edit):null,v=k=>e?esc(e[k]):"";
  return`${msg()}<div class="card"><h3 style="margin-top:0">${e?"Update employee":"Add employee"}</h3>
  <form id="f"><div class="form">
  <div><label>Employee ID</label><input name="id" value="${v("id")}" ${e?"readonly":""} placeholder="EMP1004" required></div>
  <div><label>Name</label><input name="name" value="${v("name")}" required></div>
  <div><label>Basic salary (₹)</label><input name="basic" type="number" step="any" value="${v("basic")}" required></div>
  <div><label>Allowances (₹)</label><input name="allowances" type="number" step="any" value="${v("allowances")}" required></div>
  <div><label>Performance (0–100)</label><input name="performance" type="number" step="any" value="${v("performance")}" required></div></div>
  <p style="margin-bottom:0"><button class="btn p" type="submit">${e?"Update":"Add"} employee</button></p></form></div>`}
function submit(ev){ev.preventDefault();const o=Object.fromEntries(new FormData(ev.target));
  try{const emp=Payroll.validate(o,store.map,!!edit);store.add(emp);
    flash={t:"ok",m:edit?"Employee updated successfully.":"Employee added successfully."};edit=null;tab=1;render()}
  catch(err){flash={t:"er",m:err instanceof PayrollError?err.message:"Unexpected error."};render()}}
function vSlip(){const ids=store.all();if(!slipId||!store.map.has(slipId))slipId=ids[0]?.id;
  const e=store.map.get(slipId);if(!e)return"<div class='card'>No employees available.</div>";
  const s=Payroll.salary(e),row=(a,b)=>`<dt>${a}</dt><dd>${inr(b)}</dd>`;
  return`<div class="card noprint"><label>Select employee ID</label><select onchange="slipId=this.value;render()">${ids.map(x=>`<option ${x.id===slipId?"selected":""}>${esc(x.id)}</option>`).join("")}</select></div>
  <div class="card slip"><h3 style="margin-top:0">Monthly Salary Slip</h3><p style="color:var(--mu)">${esc(e.id)} · ${esc(e.name)} · Performance ${e.performance}</p>
  <dl>${row("Basic salary",e.basic)}${row("Allowances",e.allowances)}${row("Bonus",s.bonus)}<dt><b>Gross salary</b></dt><dd><b>${inr(s.gross)}</b></dd>
  ${row("Provident fund (12%)",s.pf)}${row("Professional tax",s.pt)}${row("Income tax",s.it)}<dt><b>Total deductions</b></dt><dd><b>${inr(s.ded)}</b></dd>
  <dt class="net">Net salary</dt><dd class="net">${inr(s.net)}</dd></dl></div>
  <button class="btn noprint" onclick="try{window.print()}catch(e){}">Print slip</button>`}
function vRep(){const l=store.all().map(e=>({e,s:Payroll.salary(e)})),t=k=>l.reduce((a,x)=>a+x.s[k],0);
  return`<div class="card"><h3 style="margin-top:0">Consolidated Payroll Report</h3><div class="tw"><table>
  <tr><th>ID</th><th>Name</th><th class="n">Gross</th><th class="n">PF</th><th class="n">Prof. tax</th><th class="n">Income tax</th><th class="n">Net</th></tr>
  ${l.map(({e,s})=>`<tr><td>${esc(e.id)}</td><td>${esc(e.name)}</td><td class="n">${inr(s.gross)}</td><td class="n">${inr(s.pf)}</td><td class="n">${inr(s.pt)}</td><td class="n">${inr(s.it)}</td><td class="n">${inr(s.net)}</td></tr>`).join("")}
  <tr><th colspan="2">Total</th><th class="n">${inr(t("gross"))}</th><th class="n">${inr(t("pf"))}</th><th class="n">${inr(t("pt"))}</th><th class="n">${inr(t("it"))}</th><th class="n">${inr(t("net"))}</th></tr></table></div></div>
  <button class="btn noprint" onclick="try{window.print()}catch(e){}">Print report</button>`}
function vTax(){let p=0;return`<div class="card"><h3 style="margin-top:0">Company-defined demo tax slabs (monthly gross)</h3><div class="tw"><table><tr><th>From</th><th>To</th><th class="n">Rate</th></tr>
  ${TAX_SLABS.map(([l,r])=>{const x=`<tr><td>${inr(p)}</td><td>${l===Infinity?"and above":inr(l)}</td><td class="n">${r*100}%</td></tr>`;p=l;return x}).join("")}</table></div>
  <p style="color:var(--mu)">PF = 12% of basic. Professional tax = ₹200 when gross exceeds ₹15,000. Bonus: 15% (perf ≥ 90), 10% (≥ 75), 5% (≥ 60), else 0.</p></div>`}
function vTest(){const cases=[];const eq=(n,a,b)=>cases.push([n,Math.abs(a-b)<.005,a,b]);
  const th=(n,f)=>{let ok=false;try{f()}catch(e){ok=e instanceof PayrollError}cases.push([n,ok,"error","error"])};
  const m=new Map([["EMP1001",1]]);
  eq("Tax at ₹25,000 = 0",Payroll.tax(25000),0);eq("Tax at ₹41,000 = 800",Payroll.tax(41000),800);
  eq("Tax at ₹55,000 = 1,750",Payroll.tax(55000),1750);eq("Tax at ₹150,000 = 12,500",Payroll.tax(150000),12500);eq("Tax at ₹0 = 0",Payroll.tax(0),0);
  eq("Bonus perf 90 = 15%",Payroll.bonus(1000,90),150);eq("Bonus perf 89 = 10%",Payroll.bonus(1000,89),100);eq("Bonus perf 60 = 5%",Payroll.bonus(1000,60),50);eq("Bonus perf 59 = 0",Payroll.bonus(1000,59),0);
  eq("EMP1001 net = 36,400",Payroll.salary(new Employee("E","x",30000,8000,80)).net,36400);
  eq("EMP1002 net = 48,250",Payroll.salary(new Employee("E","x",40000,9000,92)).net,48250);
  eq("EMP1003 net = 28,615",Payroll.salary(new Employee("E","x",26000,5000,65)).net,28615);
  eq("No prof. tax at gross ₹10,000",Payroll.salary(new Employee("E","x",10000,0,0)).pt,0);
  th("Rejects bad ID",()=>Payroll.validate({id:"X1",name:"Ann",basic:1,allowances:0,performance:0},m));
  th("Rejects duplicate ID",()=>Payroll.validate({id:"emp1001",name:"Ann",basic:1,allowances:0,performance:0},m));
  th("Rejects negative allowances",()=>Payroll.validate({id:"EMP2000",name:"Ann",basic:1,allowances:-1,performance:0},m));
  th("Rejects performance > 100",()=>Payroll.validate({id:"EMP2000",name:"Ann",basic:1,allowances:0,performance:101},m));
  th("Rejects non-numeric basic",()=>Payroll.validate({id:"EMP2000",name:"Ann",basic:"abc",allowances:0,performance:0},m));
  th("Rejects empty name",()=>Payroll.validate({id:"EMP2000",name:" ",basic:1,allowances:0,performance:0},m));
  const pass=cases.filter(c=>c[1]).length;
  return`<div class="card"><h3 style="margin-top:0">Automated test cases: <span class="${pass===cases.length?"t-ok":"t-er"}">${pass}/${cases.length} passed</span></h3><div class="tw"><table><tr><th>Test</th><th>Result</th></tr>
  ${cases.map(c=>`<tr><td>${esc(c[0])}</td><td class="${c[1]?"t-ok":"t-er"}">${c[1]?"PASS":"FAIL"}</td></tr>`).join("")}</table></div></div>`}
render();
</script></body></html>
