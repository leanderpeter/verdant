import './App.css';
import Stickyfooter from './components/footer';
import SignUp from './components/signUp';
import { CssBaseline, ThemeProvider } from '@material-ui/core';
import Theme from './Theme';

function App() {
  return (
    <div>
      <ThemeProvider theme={Theme}>
        <CssBaseline />
          <SignUp/>
          <Stickyfooter/>
      </ThemeProvider>
    </div>
  );
}



export default App;
