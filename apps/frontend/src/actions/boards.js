import axios from 'axios';
import { GET_BOARDS, DELETE_BOARD, ADD_BOARD, GET_ERRORS} from './types'
import { createMessage } from './messages'

export const getBoards = () => dispatch => {
    axios
      .get("/boards/")
      .then(res => {
          dispatch({
              type: GET_BOARDS,
              payload: res.data
          })
      })
      .catch(err => console.log(err));
}

export const deleteBoard = (id) => dispatch => {
    axios
      .delete(`/boards/${id}`)
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
    axios.post("/boards/")
      .then(res=> {
          dispatch({
              type:ADD_BOARD,
              paylod: res.data
          })
      })
      .catch(err => {
          const errors = {
              msg: err.response.data,
              status: err.response.status
          }
          dispatch({
              type: GET_ERRORS,
              payload: errors
          })
      });
}