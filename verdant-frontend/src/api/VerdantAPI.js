import SignUpBO from './SignUpBO';


/*
Singleton Abstarktion des backend REST interfaces. Es handelt sich um eine access methode
*/
export default class VerdantAPI{
    //singletone instance
	static #api = null;

	// Lokales Python backend
	#VerdantServerBaseURL = '/VerdantApp';

    // ------------------------ GET ------------------------------
    #getSignUpByEmail = (email) => `${this.#VerdantServerBaseURL}/signUp/${email}`;


    // ------------------------ POST -----------------------------
    #postSignUp = () => `${this.#VerdantServerBaseURL}/signUp`;

    /*
	Singleton/Einzelstuck instanz erhalten
	*/
	static getAPI() {
		if (this.#api == null) {
			this.#api = new VerdantAPI();
		} 
		return this.#api;
	}

    /*
	Gibt einen Error zuruck auf JSON Basis. fetch() gibt keine Errors wie 404 oder 500 zuruck. Deshaltb die func fetchAdvanced 
	*/
	#fetchAdvanced = (url, init) => fetch(url, init, {credentials: 'include'})
    .then(res => {
        //fetch() gibt keine Errors wie 404 oder 500 zuruck
        if (!res.ok) {
            throw Error(`${res.status} ${res.statusText}`);
            //throw Error(`Fail`);
        }
        return res.json();
    })

    addSignUp(signUpBO) {
		return this.#fetchAdvanced(this.#postSignUp(), {
			method: 'POST',
			headers: {
				'Accept': 'application/json, text/plain',
				'Content-type': 'application/json',
			},
			body: JSON.stringify(signUpBO)
		}).then((responseJSON) => {
			// zuruck kommt ein array, wir benoetigen aber nur ein Objekt aus dem array
			let responseSignUpBO = SignUpBO.fromJSON(responseJSON);
			return new Promise(function (resolve) {
				resolve(responseSignUpBO);
			})
		})
	}

}