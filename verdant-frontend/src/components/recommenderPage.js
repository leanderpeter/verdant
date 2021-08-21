import React, { useEffect, useState } from "react";
import Grid from "@material-ui/core/Grid";
import { makeStyles } from "@material-ui/core/styles";
import Autocomplete from "@material-ui/lab/Autocomplete";
import TextField from "@material-ui/core/TextField";
import VerdantAPI from "../api/VerdantAPI";
import Button from "@material-ui/core/Button";
import LinearProgress from "@material-ui/core/LinearProgress";
import RecommendationDialog from "../dialogs/RecommendationsDialog";

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  paper: {
    padding: theme.spacing(2),
    textAlign: "center",
    color: theme.palette.text.secondary,
  },
  searchBar: {
    width: 500,
    "& > * + *": {
      marginTop: theme.spacing(3),
    },
  },
}));

export default function RecommenderLandingPage({}) {
  const [stocksMetadata, setStocksMetadata] = useState([]);
  const [error, setError] = useState(null);
  const classes = useStyles();
  const [stockChoosen, setChosenStocks] = useState([]);
  const [prediction, setPrediction] = useState([]);
  const [loadingInProgress, setLoadingInProgress] = useState(false);

  // dialog handling
  const [open, setOpen] = useState(false);
  const [selectedValue, setSelectedValue] = useState("analkopf");

  const handleClickOpen = () => {
    setOpen(true);
  };

  const handleClose = (value) => {
    setOpen(false);
    setSelectedValue(value);
  };

  const getAllStockMetadata = () => {
    VerdantAPI.getAPI()
      .getAllStockMetadata()
      .then((StockMetadata) => {
        setStocksMetadata(StockMetadata);
      })
      .catch((e) => {
        setError(e);
        console.log(error);
      });
  };

  const sendRequest = (stockList) => {
    VerdantAPI.getAPI()
      .getStockPrediction(stockList)
      .then((respon) => {
        setPrediction(respon);
        handleClickOpen();
        setLoadingInProgress(false);
      })
      .catch((e) => {
        setPrediction(null);
        setError(e);
        setLoadingInProgress(false);
      });
    setLoadingInProgress(true);
  };

  const putRequest = () => {
    if (stockChoosen.length > 2) {
      var stockList = [];
      stockChoosen.forEach(function (stock) {
        var tmp = {
          id: 1,
          uuid: "TEST2",
          ticker: stock.getTickerSymbol(),
          interaction_name: stock.getTickerSymbol(),
        };
        stockList.push(tmp);
      });
      sendRequest(stockList);
    } else {
      alert("Select more than 2 stocks");
    }
  };

  useEffect(() => {
    getAllStockMetadata();
  }, []);

  return (
    <div className={classes.root}>
      <Grid
        container
        direction="row"
        justify="center"
        alignItems="center"
        style={{ minHeight: "100vh" }}
      >
        <Grid
          container
          direction="column"
          justify="center"
          alignItems="center"
          style={{ minHeight: "100vh" }}
        >
          <Grid item>
            <h1>Verdant Stock-Picker Beta</h1>
          </Grid>
          <Grid item>
            <Autocomplete
              className={classes.searchBar}
              multiple
              id="tags-standard"
              options={stocksMetadata}
              onChange={(e, v) => setChosenStocks(v)}
              getOptionLabel={(option) => option.ticker}
              renderInput={(params) => (
                <TextField
                  {...params}
                  variant="standard"
                  label="Enter your favorite Stock Ticker"
                  placeholder="TSLA, AMZN ..."
                />
              )}
            />
            {loadingInProgress ? (
              <>
                <LinearProgress color="secondary" />
              </>
            ) : null}
          </Grid>
          <Grid item>
            <Button onClick={putRequest}>Search</Button>
          </Grid>
          <RecommendationDialog
            selectedValue={selectedValue}
            open={open}
            onClose={handleClose}
            stocks={prediction}
          />
        </Grid>
      </Grid>
    </div>
  );
}
