import React, { Component } from 'react';
import {Link} from "react-router-dom";
import { connect } from "react-redux";
import PropTypes from 'prop-types';
import { logout } from '../actions/users'

class Header extends Component {
    static propTypes = {
        users: PropTypes.object.isRequired,
        logout: PropTypes.func.isRequired
    }
    render() {
        const { isAuthenticated, user } = this.props.user;
        const authLinks = (
            <ul className="navbar-nav mr-auto mt-2 mt-lg-0">
                <li className="nav-item">
                    <button 
                      onClick={this.props.logout}
                      className="nav-link btn btn-info btn-sm text-light" >
                      logout
                      </button>
                </li>
            </ul>
        )
        const guestLink = (
            <ul className="navbar-nav mr-auto mt-2 mt-lg-0">
                <li className="nav-item">
                    <Link to="/register" className="nav-link">Resiter</Link>
                </li>
                <li className="nav-item">
                    <Link to="/login" className="nav-link">Login</Link>
                </li>
            </ul>
        )
        return (
            <nav className="navbar navbar-expand-sm navbar-light bg-light">
                <div className="container">
                    <button
                        className="navbar-toggler"
                        type="button"
                        data-toggle="collapse"
                        data-target="#navbarTogglerDemo01"
                        aria-controls="navbarTogglerDemo01"
                        aria-expanded="false"
                        aria-label="Toggle navigation">
                        <span className="navbar-toggler-icon"></span>
                    </button>
                    <div className="collapse navbar-collapse" id="navbarTogglerDemo01">
                        <a className="navbar-brand" href="/">Lead Manager</a>
                    </div>
                    {isAuthenticated ? authLinks : guestLink}
                </div>
            </nav>
        )
    }
}

const mapStateToProps = state =>({
    user: state.users
})

export default connect(mapStateToProps, { logout })(Header);