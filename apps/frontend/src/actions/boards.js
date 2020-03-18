import axios from 'axios';
import { GET_BOARDS, DELETE_BOARD} from './types'

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
          dispatch({
              type: DELETE_BOARD,
              payload: id
          })
      })
      .catch(err => console.log(err))
}