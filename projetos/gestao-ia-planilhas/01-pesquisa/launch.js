const {chromium}=require('playwright');
module.exports=async function launch(extra=[]){
  return await chromium.launch({executablePath:'/opt/pw-browsers/chromium', headless:true, timeout:25000,
    proxy:{server:'http://127.0.0.1:46127', bypass:'localhost,127.0.0.1'},
    args:['--no-sandbox','--disable-dev-shm-usage','--disable-gpu','--ssl-version-max=tls1.2',
      '--disable-features=UseMLKEM,PostQuantumKyber','--disable-background-networking','--disable-component-update',
      '--no-first-run','--disable-sync','--metrics-recording-only','--no-default-browser-check',...extra]});
}
