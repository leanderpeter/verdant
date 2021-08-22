import React from "react";
import PropTypes from "prop-types";
import { makeStyles } from "@material-ui/core/styles";
import Button from "@material-ui/core/Button";
import Avatar from "@material-ui/core/Avatar";
import List from "@material-ui/core/List";
import ListItem from "@material-ui/core/ListItem";
import ListItemAvatar from "@material-ui/core/ListItemAvatar";
import ListItemText from "@material-ui/core/ListItemText";
import DialogTitle from "@material-ui/core/DialogTitle";
import Dialog from "@material-ui/core/Dialog";
import PersonIcon from "@material-ui/icons/Person";
import AddIcon from "@material-ui/icons/Add";
import Typography from "@material-ui/core/Typography";
import { blue } from "@material-ui/core/colors";
import AccountBalanceIcon from "@material-ui/icons/AccountBalance";
import ShowChartIcon from "@material-ui/icons/ShowChart";

const emails = ["username@gmail.com", "user02@gmail.com"];
const useStyles = makeStyles({
  avatar: {
    backgroundColor: blue[100],
    color: blue[600],
  },
});

export default function RecommendationDialog(props) {
  const classes = useStyles();
  const { onClose, selectedValue, open, stocks } = props;
  const handleClose = () => {
    onClose(selectedValue);
  };

  const handleListItemClick = (value) => {
    //onClose(value);
    console.log(value.ticker);
    openInNewTab("https://finance.yahoo.com/quote/" + value.ticker);
    //https://finance.yahoo.com/quote/TSLA/
  };

  const openInNewTab = (url) => {
    const newWindow = window.open(url, "_blank", "noopener,noreferrer");
    if (newWindow) newWindow.opener = null;
  };

  return (
    <Dialog
      onClose={handleClose}
      aria-labelledby="simple-dialog-title"
      open={open}
    >
      <DialogTitle id="simple-dialog-title">
        Your stock recommendations:
      </DialogTitle>
      <List>
        {stocks.map((stock) => (
          <ListItem
            button
            onClick={() => handleListItemClick(stock)}
            key={stock}
          >
            <ListItemAvatar>
              <Avatar className={classes.avatar}>
                <ShowChartIcon />
              </Avatar>
            </ListItemAvatar>
            <ListItemText primary={stock.ticker} />
          </ListItem>
        ))}
      </List>
    </Dialog>
  );
}

RecommendationDialog.propTypes = {
  onClose: PropTypes.func.isRequired,
  open: PropTypes.bool.isRequired,
  selectedValue: PropTypes.string.isRequired,
};
