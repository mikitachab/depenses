import React from 'react';
import axios from "axios";
import { Redirect } from "react-router-dom";

class SignUp extends React.Component {
    constructor() {
        super();
        this.state = {
            userName: "",
            email: "",
            password: "",
            confirmPassword: "",
            validatePassword: false
        };
        this.userNameRef = React.createRef();
        this.userEmailRef = React.createRef();
        this.userPasswordRef = React.createRef();
        this.userPasswordConfirmedRef = React.createRef();
    }



    handleUserNameChange = () => {
        this.setState({ userName: this.userNameRef.current.value });
        console.log(this.state.userName);
    }

    handleEmailChange = () => {
        this.setState({ email: this.userEmailRef.current.value });
    }

    handlePasswordChange = () => {
        console.log(this.userPasswordRef.current.value);
        this.setState({ password: this.userPasswordRef.current.value });
    }

    handlePasswordConfirmedChange = () => {
        this.setState({ confirmPassword: this.userPasswordConfirmedRef.current.value });
    }


    validateForm = () => {
        if (this.state.password !== this.state.confirmPassword) {
            this.state.validatePassword = false;
        } else if (this.state.password === this.state.confirmPassword) {
            this.state.validatePassword = true;
        }
        return (
            this.state.userName.length > 0 &&
            this.state.email.length > 0 &&
            this.state.validatePassword
        );
    }

    handleSubmit = (e) => {
        e.preventDefault();

        axios.post('http://127.0.0.1:8000/api/auth/users/',
            {
                username: this.state.userName,
                email: this.state.email,
                password: this.state.password
            }).then(response => {
                console.log(response);
                if (response.status === 200) {
                    console.log(response);
                    this.setState({ redirect: '/Login' })
                }
            })
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
                            <h1 className="text-center">SingUp</h1>
                            <div className="card-body">
                                <form className="text-center" action="#!" onSubmit={this.handleSubmit}>
                                    <div className="md-form">
                                        <input ref={this.userNameRef}
                                            onChange={this.handleUserNameChange}
                                            id="input-name" className="form-control" placeholder="Name" />
                                    </div>
                                    <div className="md-form">
                                        <input ref={this.userEmailRef}
                                            onChange={this.handleEmailChange}
                                            id="input-email" className="form-control" placeholder="E-mail" />
                                    </div>
                                    <div className="md-form">
                                        <input ref={this.userPasswordRef}
                                            onChange={this.handlePasswordChange}
                                            type="password" id="input-password" className="form-control" placeholder="Password" />
                                    </div>
                                    <div className="md-form">
                                        <input ref={this.userPasswordConfirmedRef}
                                            onChange={this.handlePasswordConfirmedChange}
                                            type="password" id="input-password" className="form-control" placeholder="Confirm Password" />
                                    </div>

                                    <button
                                        href="/"
                                        className="btn btn-dark btn-rounded btn-block my-4 waves-effect z-depth-0"
                                        type="submit"
                                        disabled={!this.validateForm()}>
                                        SignUp
                                    </button>

                                    <p>Do you have an account?
                                        <a href="/signin">
                                            Log in
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



export default SignUp;
