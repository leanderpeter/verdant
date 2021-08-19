import React, { Component } from "react";
import PropTypes from "prop-types";
import {
  withStyles,
  Typography,
  Button,
  InputAdornment,
  TextField,
  Paper,
  Grid,
} from "@material-ui/core";
import background from "../media/background_4.jpg";
import Box from "@material-ui/core/Box";

import { VerdantAPI, SignUpBO } from "../api";

class SignUp extends Component {
  constructor(props) {
    super(props);

    this.state = {
      name: "",
      email: "",
      nameError: false,
      emailError: false,
    };
  }

  validate(email) {
    const regex =
      /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

    if (regex.test(email)) {
      console.log("passt");
      return false;
    } else {
      console.log("Fehler");
      return true;
    }
  }

  handleEmailChange = (event) => {
    this.setState({
      email: event.target.value,
    });
  };

  handleSubmit = (event) => {
    if (this.validate(this.state.email)) {
      this.setState({
        emailError: true,
      });
    } else {
      this.setState({
        emailError: false,
      });

      this.addSignUp();
      //alert(`${this.state.email}`)
    }
  };

  addSignUp = () => {
    let newSignUp = new SignUpBO();
    newSignUp.setID(0);
    newSignUp.setname(this.state.name);
    newSignUp.set_email(this.state.email);
    VerdantAPI.getAPI()
      .addSignUp(newSignUp)
      .then((signup) => {
        this.props.onClose(signup);
      })
      .catch((e) => alert(e));
  };

  componentDidMount() {}

  componentDidUpdate() {}

  render() {
    const { classes } = this.props;
    const { name, email } = this.state;

    return (
      <div className={classes.root}>
        <Box style={sectionStyle}>
          <form onSubmit={this.handleSubmit}>
            <Box>
              <Grid
                container
                spacing={0}
                direction="column"
                alignItems="center"
                justify="center"
                style={{ minHeight: "100vh" }}
              >
                <Grid Item xs={3}>
                  <Typography variant="h2" color="secondary">
                    Verdant
                  </Typography>
                </Grid>

                <Box width="50%">
                  <Grid>
                    <Typography
                      variant="subtitle1"
                      color="primary"
                      align="center"
                      textAlign="center"
                    >
                      Enter your email and service address below to participate
                      in Verdant's beta program. If service is not yet available
                      in your area, we will notify you when it becomes
                      available. Learn more about Verdant beta program here.
                    </Typography>
                  </Grid>

                  <Grid item xs={12}>
                    <TextField
                      value={this.state.email}
                      required
                      onChange={this.handleEmailChange}
                      fullWidth
                      required
                      id="standard-required"
                      label="Email Adress"
                      defaultValue=""
                      error={this.state.emailError === true}
                    />
                  </Grid>

                  <Grid item xs={12}>
                    <TextField
                      fullWidth
                      required
                      id="standard-required"
                      label="Name"
                      defaultValue=""
                    />
                  </Grid>
                </Box>

                <Box display="flex" justifyContent="center" m={0} p={4}>
                  <Button
                    type="submit"
                    color="primary"
                    variant="outlined"
                    size="large"
                  >
                    SIGN UP
                  </Button>
                </Box>
              </Grid>

              <Box display="flex" justifyContent="center" m={-20} p={12}>
                <Typography>
                  By clicking SIGNUP, you agree to our Privacy Policy.{" "}
                </Typography>
              </Box>
            </Box>
          </form>
        </Box>
      </div>
    );
  }
}

var sectionsStyles = {
  height: "100vh",
};

var sectionStyle = {
  width: "100%",
  height: "100%",
  backgroundPosition: "center",
  backgroundSize: "cover",
  backgroundImage: `url(${background})`,
};
/*
var sectionStyle = {
    display: 'flex',
    width: "100%",
    marginTop: '1000px',
    backgroundImage: `url(${'../media/background_2.jpg'})`
  };
*/

const styles = (theme) => ({
  root: {
    width: "100%",
    marginTop: theme.spacing(0),
    paddingTop: "4px",
    flexGrow: 1,
  },
  paper: {
    padding: theme.spacing(2),
    textAlign: "center",
    color: theme.palette.text.secondary,
  },
  bgImg: {
    diplay: "flex",
    width: "100%",
    backgroundImage: `url(${background})`,
  },
  textField: {
    marginLeft: theme.spacing(1),
    marginRight: theme.spacing(1),
    width: "25ch",
  },
});

export default withStyles(styles)(SignUp);
