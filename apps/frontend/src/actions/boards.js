import axios from 'axios';
import {GET_BOARDS} from './types'

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