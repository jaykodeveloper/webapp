import { GET_BOARDS } from "../actions/types.js";

const initialState = {
    boards : []
}

export default function(state=initialState, action) {
    switch (action.type) {
        case GET_BOARDS:
            return{
                ...state,
                boards: action.payload
            }
            default:
                return state;
    }
}