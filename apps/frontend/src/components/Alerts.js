import React, { Component, Fragement } from 'react';
import { withAlert } from 'react-alert';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';

export class Alerts extends Component {
    static propTypes = {
        error: PropTypes.object.isRequired,
        message: PropTypes.object.isRequired
    }

    componentDidMount() {
        const {error, alert, message } = this.props;
        if(error !== prevProps.error){
            if(error.msg.title) alert.error(`Title: ${error.msg.title.join()}`);
            if(error.msg.image) alert.error(`Image: ${error.msg.image.join()}`);
            if(error.msg.detail) alert.error("Credential needed!")
        }
        if(message !== prevProps.message){
            if(message.deletedBoard) alert.success(message.deletedBoard);
        }
    }
    render(){
        return <Fragement />;
    }
}

const mapStateToProps = state => ({
    error: state.errors,
    message: state.messages
})

export default connect(mapStateToProps)(withAlert()(Alerts));