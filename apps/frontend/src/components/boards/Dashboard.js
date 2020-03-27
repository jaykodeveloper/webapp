import React, { Fragment, Component } from 'react';
import { HashRouter as Router, Route, Switch } from 'react-router-dom';
import CreateBoard from './CreateBoard';
import BoardList from './BoardList';
import Board from './Board'

export default function Dashboard() {
    return(
        <Router>
            <Fragment>
                <CreateBoard />
                <BoardList />
                <Route exact path="/boards/:id" component={Board} />
            </Fragment>
        </Router>
    )
}