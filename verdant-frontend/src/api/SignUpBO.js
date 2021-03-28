import NamedBusinessObject from './NamedBusinessObject';

export default class SignUpBO extends NamedBusinessObject{
    constructor(aemail){
        super();
        this.email = aemail;
    }

    get_email(){
        return this.email;
    }

    set_email(aemail){
        this.email = aemail;
    }

	static fromJSON(signup) {
		let results = null;
		if (Array.isArray(signup)) {
			results = [];
			signup.forEach((c) => {
				Object.setPrototypeOf(c, SignUpBO.prototype);
				results.push(c);
			})
		} else {
			// Es gibt wohl nur ein Objekt
			let c = signup;
			Object.setPrototypeOf(c, SignUpBO.prototype);
			results = c;
		}
		return results;
	}
}