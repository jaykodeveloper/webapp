import { combineReducers } from 'redux';
import boards from './boards';
import errors from './errors';
import messages from "./messages"

export default combineReducers({
    boards,
    errors,
    messages
});