import React, { Component, Fragment } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import {Link} from "react-router-dom";

import { getBoards, deleteBoard } from "../../actions/boards"
import Board from "./Board"

export class BoardList extends Component {
    static propTypes = {
        boards: PropTypes.array.isRequired,
        getBoards: PropTypes.func.isRequired,
        deleteBoard: PropTypes.func.isRequired,
    }
    componentDidMount() {
        this.props.getBoards();
    }

    render() {
        this.props.boards.sort((boardA, boardB) => { return boardA.id - boardB.id });
        const sortedRows = this.props.boards.map(board => {
            return (
                <tr key={board.id}>
                    <td>{board.id}</td>
                    <td>{board.author}</td>
                    <td>
                        <Link to={`/boards/${board.id}`} className="nav-link">{board.title}</Link>
                    </td>
                    <td>{board.created}</td>
                    <td>{board.updated}</td>
                    <td>
                        <button className="btn btn-danger btn-sm" onClick={this.props.deleteBoard.bind(this, board.id)}>
                            Delete
                        </button>
                    </td>
                </tr>
            )
        });
        return (
            <Fragment>
                <h2>Boards</h2>
                <table className="table table-striped">
                    <thead>
                        <tr>
                            <th>Num.</th>
                            <th>Author</th>
                            <th>Title</th>
                            <th>Created</th>
                            <th>Updated</th>
                            <th />
                        </tr>
                    </thead>
                    <tbody>
                    {this.props.boards.length > 0 && (sortedRows)}
                    </tbody>
                </table>
            </Fragment>
        )
    }
}

const mapStateToProps = state => ({
    boards: state.boards.boards
})

export default connect(mapStateToProps, {getBoards, deleteBoard})(BoardList)