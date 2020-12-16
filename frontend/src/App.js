import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import SignIn from './components/auth/SignIn';
import SignUp from './components/auth/SignUp';
import MainPage from './components/mainpage/MainPage';
import './styles/main.scss';

class App extends React.Component {
  render() {
    return (
      <Router>
        <Switch>
          <Route path='/' exact component={MainPage} />
          <Route path='/signin' component={SignIn} />
          <Route path='/signup' component={SignUp} />
        </Switch>
      </Router>
    );
  }
}



export default App;
