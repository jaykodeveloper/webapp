import axios from 'axios';
import { GET_BOARDS, DELETE_BOARD, ADD_BOARD } from './types'
import { createMessage, returnErrors } from './messages'

export const getBoards = () => dispatch => {
    axios
      .get("api/boards/")
      .then(res => {
          dispatch({
              type: GET_BOARDS,
              payload: res.data
          })
      })
      .catch(err => dispatch(returnErrors(err.response.data, err.response.status)));
}

export const deleteBoard = (id) => dispatch => {
    axios
      .delete(`api/boards/${id}`)
      .then(res => {
          dispatch(createMessage({ deleteBoard: "Board Deleted"}))
          dispatch({
              type: DELETE_BOARD,
              payload: id
          })
      })
      .catch(err => console.log(err))
}

export const addBoard = () => dispatch => {
    axios.post("api/boards/")
      .then(res=> {
          dispatch({
              type:ADD_BOARD,
              paylod: res.data
          })
      })
      .catch(err => dispatch(returnErrors(err.response.data, err.response.status)));
}