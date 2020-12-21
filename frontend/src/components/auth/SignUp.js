import React from 'react';
import axios from "axios";
import { Redirect } from "react-router-dom";
import SuccessSignedUp from './SuccessSignedUp';

class SignUp extends React.Component {
    constructor() {
        super();
        this.state = {
            userName: "",
            email: "",
            password: "",
            confirmPassword: "",
            errorMessageEmail: "",
            errorMessagePassword: "",
            errorMessageUsername: "",
            validatePassword: false,
            succeedSingUp: false
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
            this.setState({ validatePassword: false })
        } else if (this.state.password === this.state.confirmPassword) {
            this.setState({ validatePassword: true })
        }
        return (
            this.state.userName.length > 0 &&
            this.state.email.length > 0 &&
            this.state.validatePassword
        );
    }

    handleSubmit = async (e) => {
        e.preventDefault();
        this.setState({ errorMessageEmail: '', errorMessagePassword: '' });

        try {
            const response = await axios.post('http://127.0.0.1:8000/api/auth/users/',
                {
                    username: this.state.userName,
                    email: this.state.email,
                    password: this.state.password
                })
            if (response.status === 201) {
                this.setState({ succeedSingUp: true })
            }
        } catch (error) {
            let arr = Object.entries(error.response.data);
            arr.map(el => {
                if (el[0] === 'email') {
                    this.setState({ errorMessageEmail: el[1] });
                } else if (el[0] === 'password') {
                    this.setState({ errorMessagePassword: el[1] })
                } else if (el[0] === 'username') {
                    this.setState({ errorMessageUsername: el[1] })
                }
                return arr;
            })
        }
    }

    render() {
        if (this.state.redirect) {
            return <Redirect to={this.state.redirect} />
        }
        return (
            <div>
                {
                    this.state.succeedSingUp ? <SuccessSignedUp /> :
                        <div className="container-fluid login">
                            <div className="container">
                                <div className="row">
                                    <div className="card">
                                        <h1 className="text-center">SingUp</h1>
                                        <div className="card-body">
                                            <form className="text-center" onSubmit={this.handleSubmit}>
                                                <div className="md-form">
                                                    <input ref={this.userNameRef}
                                                        onChange={this.handleUserNameChange}
                                                        id="input-name" className="form-control" placeholder="Name" />
                                                    {this.state.errorMessageUsername ? (<div className="error-text">{this.state.errorMessageUsername}</div>) : ""}

                                                </div>
                                                <div className="md-form">
                                                    <input ref={this.userEmailRef}
                                                        onChange={this.handleEmailChange}
                                                        id="input-email" className="form-control" placeholder="E-mail" />
                                                    {this.state.errorMessageEmail ? (<div className="error-text">{this.state.errorMessageEmail}</div>) : ""}
                                                </div>
                                                <div className="md-form">
                                                    <input ref={this.userPasswordRef}
                                                        onChange={this.handlePasswordChange}
                                                        type="password" id="input-password" className="form-control" placeholder="Password" />
                                                    {this.state.errorMessagePassword ? (<div className="error-text">{this.state.errorMessagePassword}</div>) : ""}
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
                                                    disabled={!this.validateForm}
                                                >
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
                        </div>}
            </div>
        );
    }
}



export default SignUp;
