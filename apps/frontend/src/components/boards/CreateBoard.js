import React, {Component} from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { addBoard } from '../../actions/boards';

class CreateBoard extends Component {
    constructor(props) {
        super(props)
        this.state = {
            title: '',
            body: '',
            author: '',
            image: null,
        }
    }

    static propTypes = {
        addBoard: PropTypes.func.isRequired
    }

    onSubmit = (e) => {
        e.preventDefault();
        const { title, body, author, image } = this.state;
        const board = { title, body, author, image };
        this.props.addBoard(board);
        this.setState({
            title:"",
            body: "",
            author: "",
            image: null
        })
    }


    onChange = (e) => {this.setState({ [e.target.name]: e.target.value })}

    maxSelectFile = (e) =>{
        let files = e.target.files
        if(files.length > 1) {
            const msg = "Only 1 images can be uploaded at a time"
            e.target.value = null
            console.log(msg)
            return false;
        }
        return true;
    }

    checkImageType = (e) => {
        let files = e.target.files
        let err = ''
        const types= ['image/png', 'image/jpeg', 'image/gif']
        for(var x = 0; x<files.length; x++){
            if(types.every(type => files[x].type !== type)){
                err += files[x].type + 'is not a supported a format\n'
            }
        };
        if(err !== ''){
            e.target.value = null
            console.log(err)
            return false;
        }
        return true;
    }

    handleFileInput(e) {
        var files = e.target.files
        if (this.maxSelectFile(e) && this.checkImageType(e)) {
            this.setState({
                image: files[0]
            })
        }
    }

    render(){
        const { title, body, author, image } = this.state;
        return (
            <div className="card card-body mt-4 mb-4">
                <h2>Add board</h2>
                <form onSubmit={this.onSubmit}>
                    <div className="form-group">
                        <label>Title</label>
                        <input
                          className="form-control"
                          type="text"
                          name="title"
                          onChange={this.onChange}
                          value={title}
                          />
                    </div>
                    <div className="form-group">
                        <label>Description</label>
                        <input
                          className="form-control"
                          type="text"
                          name="body"
                          onChange={this.onChange}
                          value={body}
                          />
                    </div>
                    <div className="form-group">
                        <label>Image</label>
                        <input
                          className="form-control"
                          type="file"
                          name="image"
                          onChange={this.handleFileInput}
                          value={image}
                          />
                    </div>
                    <div className="form-group">
                        <button 
                          type="submit" 
                          className="btn btn-primary"
                          onClick={this.onSubmit}>
                            Submit
                        </button>
                    </div>
                </form>
            </div>
        )
    }
}

export default connect(null, {addBoard})(CreateBoard);