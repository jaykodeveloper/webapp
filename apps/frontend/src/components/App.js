import React, { Component, Fragment } from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { Provider as AlertProvider } from 'react-alert';
import AlertTemplate from 'react-alert-template-basic';

import Header from './Header'
import Dashboard from './boards/Dashboard'
import Alerts from './Alerts'
import store from '../store';

const alertOptions = {
    timeout: 3000,
    position: 'top center'
}

class App extends Component {
    render() {
        return (
            <Provider store={store}>
                <AlertProvider template={AlertTemplate} {...alertOptions} >
                    <Fragment>
                        <Header />
                        <div className="container">
                            <Dashboard />
                        </div>
                    </Fragment>
                </AlertProvider>
            </Provider>
        )
    }
}

ReactDOM.render(<App />, document.getElementById('app'));