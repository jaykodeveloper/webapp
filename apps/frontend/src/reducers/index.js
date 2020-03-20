import { combineReducers } from 'redux';
import boards from './boards';
import errors from './errors';
import messages from "./messages"
import users from './users';

export default combineReducers({
    boards,
    errors,
    messages,
    users,
});