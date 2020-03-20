import React from 'react';
import { Route, Redirect } from 'react-router-dom';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';

const PrivateRoute = ({ component: Component, users, ...rest }) =>(
    <Route
      {...rest}
      render={props => {
          if(users.isLoading){
              return <h2>Loding ...</h2>
          } else if(!users.isAuthenticated){
              return <Redirect to="/login" />
          } else{
              return <Component {...props} />
          }
      }}
      />
)

const mapStateToProps = state => ({
    users: state.users
})

export default connect(mapStateToProps)(PrivateRoute)