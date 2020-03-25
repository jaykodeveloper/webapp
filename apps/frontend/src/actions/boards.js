import axios from 'axios';
import { GET_BOARDS, DELETE_BOARD, ADD_BOARD } from './types'
import { createMessage, returnErrors } from './messages'
import { tokenConfig } from './users'

export const getBoards = () => (dispatch, getState) => {
// export const getBoards = () => dispatch => {
    axios
    //   .get("api/boards/")
      .get("api/boards/", tokenConfig(getState))
      .then(res => {
          dispatch({
              type: GET_BOARDS,
              payload: res.data
          })
      })
      .catch(err => dispatch(returnErrors(err.response.data, err.response.status)));
}

// export const deleteBoard = (id) => dispatch => {
export const deleteBoard = (id) => (dispatch, getState) => {
    axios
    //   .delete(`api/boards/${id}`)
      .delete(`api/boards/${id}`, tokenConfig(getState))
      .then(res => {
          dispatch(createMessage({ deleteBoard: "Board Deleted"}))
          dispatch({
              type: DELETE_BOARD,
              payload: id
          })
      })
      .catch(err => console.log(err))
}

export const addBoard = board => (dispatch, getState) => {
    const token = getState().users.token;

    const config = {
        headers: {
            // "Content-Type": undefined
            // "Content-Type": "application/json"
            "Content-Type": "multipart/form-data"
        }
    }
    if(token) {
        config.headers["Authorization"] = `Token ${token}`
    }

    axios
      .post("api/boards/", board, config)
      .then(res=> {
          dispatch(createMessage({ addBoard: "Board added"}));
          dispatch({
              type:ADD_BOARD,
              payload: res.data
          })
      })
      .catch(err => dispatch(returnErrors(err.response.data, err.response.status)));
}