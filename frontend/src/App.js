import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Login from './Login';
import MainPage from './MainPage';
import './styles/main.scss';

class App extends React.Component {
  render() {
    return (
      <Router>
        <Switch>
          <Route path='/' exact component={MainPage} />
          <Route path='/login' component={Login} />
        </Switch>
      </Router>
    );
  }
}



export default App;
