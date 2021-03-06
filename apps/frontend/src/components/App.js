import React, { Component, Fragment } from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { Provider as AlertProvider } from 'react-alert';
import AlertTemplate from 'react-alert-template-basic';
import { HashRouter as Router, Route, Switch } from 'react-router-dom';

import Header from './Header'
import Dashboard from './boards/Dashboard'
// import {Alerts} from './Alerts'
import store from '../store';
import Login from './users/Login'
import SignUp from './users/SignUp'
import PrivateRoute from './PrivateRoute'
import { loadUser } from '../actions/users'

const alertOptions = {
    timeout: 3000,
    position: 'top center'
}

class App extends Component {
    componentDidMount(){
        store.dispatch(loadUser())
    }
    render() {
        return (
            <Provider store={store}>
                <AlertProvider template={AlertTemplate} {...alertOptions} >
                    <Router>
                        <Fragment>
                            <Header />
                            {/* <Alerts /> */}
                            <div className="container">
                                <Switch>
                                    <PrivateRoute exact path="/" component={Dashboard} />
                                    <Route exact path="/register" component={SignUp} />
                                    <Route exact path="/login" component={Login} />
                                </Switch>
                            </div>
                        </Fragment>
                    </Router>
                </AlertProvider>
            </Provider>
        )
    }
}

ReactDOM.render(<App />, document.getElementById('app'));