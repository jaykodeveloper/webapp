import { GET_BOARDS, DELETE_BOARD } from "../actions/types.js";

const initialState = {
    boards : []
}

export default function(state=initialState, action) {
    switch (action.type) {
        case GET_BOARDS:
            return {
                ...state,
                boards: action.payload
            }
        case DELETE_BOARD:
            return {
                ...state,
                boards:state.boards.filter(board => board.id !== action.payload)
            }
        default:
            return state;
    }
}