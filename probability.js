(function(global){
	const fac=n=>n==0?1:n*fac(n-1);
	const choose=(n,r)=>fac(n)/(fac(r)*fac(n-r))

	if(exports){
		exports.fac = fac;
		exports.choose = choose;
	} else {
		const Probabilitly = {};
		global.Probabilitly = Probabilitly;
		Probabilitly.fac = fac;
		Probabilitly.choose = choose;
	}
	
})(this);