import "./App.css";
import { CssBaseline, ThemeProvider } from "@material-ui/core";
import Theme from "./Theme";
import RecommenderLandingPage from "./components/recommenderPage";

function App() {
  return (
    <div>
      <ThemeProvider theme={Theme}>
        <CssBaseline />
        <RecommenderLandingPage />
      </ThemeProvider>
    </div>
  );
}

export default App;
