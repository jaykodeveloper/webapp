import axios from 'axios';
import {returnErrors} from "./messages";

import { 
    USER_LOADED, 
    USER_LOADING, 
    AUTH_ERROR, 
    LOGIN_SUCCESS, 
    LOGIN_FAIL,
    LOGOUT_SUCCESS,
    REGISTER_SUCCESS,
    REGISTER_FAIL
} from "./types";

export const loadUser = () => (dispatch, getState) => {
    dispatch({ type: USER_LOADING })
    const token = getState().users.token;
    const id = getState().users.id;

    const config = {
        headers: {
            'Content-Type': 'application/json'
        }
    }

    if(token) {
        config.headers['Authorization'] = `Token ${token}`;
    }

    axios.get(`/api/users/${id}`, config)
      .then(res => {
          dispatch({
              type: USER_LOADED,
              payload: res.data
          });
      }).catch(err => {
          dispatch(returnErrors(err.response.data,
            err.response.state));
          dispatch({
              type:AUTH_ERROR
          })
      })
}

export const login = (username, password) => dispatch =>{
    const config = {
        headers: {
            "Content-Type": "application/json"
        }
    }
    const body = JSON.stringify({username, password})

    axios
      .post("/api/users/accounts/login/", body, config)
      .then(res => {
          dispatch({
              type: LOGIN_SUCCESS,
              payload: res.data
          })
      })
      .catch(err => {
          dispatch(returnErrors(err.response.data, err.response.status));
          dispatch({
              type: LOGIN_FAIL
          })
      })
}

export const logout = () => (dispatch, getState) => {
    const token = getState().users.token;

    const config = {
        headers: {
            'Content-Type': 'application/json'
        }
    }

    if(token) {
        config.headers["Authorization"] = `Token ${token}`
    }

    axios
      .post("api/users/accounts/logout/", null, config)
      .then(res => {
          dispatch({
              type: LOGOUT_SUCCESS
          })
      }).catch(err => {
          dispatch(returnErrors(err.response.data, err.response.state))
      })
}

export const register = ({ username, password, email }) => dispatch => {
    const config = {
        headers: {
            'Content-Type': 'application/json'
        }
    };

    const body = JSON.stringify({ username, email, password})

    axios
      .post('/api/users/accounts/register/', body, config)
      .then(res =>{
          dispatch({
              type: REGISTER_SUCCESS,
              payload: res.data
          })
      }).catch(err => {
          dispatch(returnErrors(err.response.data, err.response.state));
          dispatch({
              type: REGISTER_FAIL
          })
      })
}