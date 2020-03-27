import React, { Component, Fragment } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { getBoard } from "../../actions/boards"

export class Board extends Component {
    constructor(props){
        super(props)
    }

    render(){
        return(
            <div>
                Hello
            </div>
        )
    }
}

export default Board;