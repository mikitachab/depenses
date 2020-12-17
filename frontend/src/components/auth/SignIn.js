import React from 'react';
import axios from "axios";
import { Redirect } from "react-router-dom";

class SignIn extends React.Component {
    constructor() {
        super();
        this.handlePasswordChange = this.handlePasswordChange.bind(this);
        this.handleEmailChange = this.handleEmailChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.state = {
            inputPassword: "",
            inputEmail: "",
            redirect: null
        };
    }

    handleEmailChange(e) {
        this.setState({ inputEmail: e.target.value });
    }

    handlePasswordChange(e) {
        this.setState({ inputPassword: e.target.value });
    }

    handleSubmit(e) {
        e.preventDefault();

        axios.post('http://127.0.0.1:8000/api/auth/token/login/',
            {
                "username": this.state.inputEmail,
                "password": this.state.inputPassword
            }
        ).then(response => {
            if (response.status === 200) {
                window.localStorage.setItem('x-auth-token', response.data.auth_token);
                this.setState({ redirect: '/' })
            }
        }

        );
    }

    render() {
        if (this.state.redirect) {
            return <Redirect to={this.state.redirect} />
        }
        return (
            <div className="container-fluid login">
                <div className="container">
                    <div className="row">
                        <div className="card">
                            <h1 className="text-center">SingIn</h1>
                            <div className="card-body">
                                <form className="text-center" action="#!" onSubmit={this.handleSubmit}>
                                    <div className="md-form">
                                        <input id="input-email" className="form-control" placeholder="E-mail" value={this.state.inputEmail} onChange={this.handleEmailChange} />
                                    </div>
                                    <div className="md-form">
                                        <input type="password" id="input-password" className="form-control" placeholder="Password" value={this.state.inputPassword} onChange={this.handlePasswordChange} />
                                    </div>

                                    <button href="/" className="btn btn-dark btn-rounded btn-block my-4 waves-effect z-depth-0" type="submit">SignIn</button>

                                    <p>Not a member?
                                        <a href="/signup">
                                            Register
                                        </a>
                                    </p>
                                </form>
                            </div>
                        </div>
                    </div>
                </div >
            </div>
        );
    }
}



export default SignIn;
