import React, { Component } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { getBoards } from "../../actions/boards"

export class BoardList extends Component {
    static propTypes = {
        boards: PropTypes.array.isRequired
    }
    componentDidMount() {
        this.props.getBoards();
    }
    render(){
        return (
            <div>
                Board List
            </div>
        )
    }
}

const mapStateToProps = state => ({
    boards: state.boards.boards
})

export default connect(mapStateToProps, {getBoards})(BoardList)