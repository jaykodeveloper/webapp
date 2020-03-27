import React, { Component, Fragment } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { getBoard } from "../../actions/boards"

export class Board extends Component {
    static propTypes = {
        getBoard : PropTypes.func.isRequired,
        board: PropTypes.object
    }

    componentDidMount(){
        this.props.getBoard();
    }

    render(){
        return(
            <div>
            {this.props.board.title}
            </div>
        )
    }
}

const mapStateToProps = state => ({
    board: state.boards
})

export default connect(mapStateToProps, {getBoard})(Board)