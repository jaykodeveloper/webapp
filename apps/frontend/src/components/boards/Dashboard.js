import React, { Fragment, Component } from 'react';
import CreateBoard from './CreateBoard';
import BoardList from './BoardList';

export default function Dashboard() {
    return(
        <Fragment>
            <CreateBoard/>
            <BoardList />
        </Fragment>
    )
}