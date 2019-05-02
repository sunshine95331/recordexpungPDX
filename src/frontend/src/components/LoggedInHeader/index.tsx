import React from 'react';
import LogOut from '../LogOut';

class LoggedInHeader extends React.Component {
  public render() {
    return (
      // The following was copy/pasted directly from http://dev.huntermarcks.net/search/
      // and should be treated only as a draft.
      <nav className="center pt4 ph2 bg-white shadow">
        <div className="mw8 center flex-l justify-between">
          <div className="mb4">

            {/* The logo should probably get extracted into its own Component. */}
            <svg className="logo" width="116" height="41" viewBox="0 0 116 41" xmlns="http://www.w3.org/2000/svg" aria-labelledby="title" aria-describedby="description" role="presentation">
              <title id="title">Record Expunge Logo</title>
              <desc id="description">Record Expunge Logo</desc>
              <defs>
                <linearGradient x1="91.276%" y1="143.962%" x2="12.051%" y2="143.962%" id="a"><stop stopColor="#65B5F0" stopOpacity="0" offset="0%"></stop><stop stopColor="#357EDD" offset="100%"></stop></linearGradient><linearGradient x1="63.216%" y1="143.962%" x2="0%" y2="143.962%" id="b"><stop stopColor="#65B5F0" stopOpacity="0" offset="0%"></stop><stop stopColor="#357EDD" offset="100%"></stop></linearGradient><linearGradient x1="100%" y1="143.962%" x2="41.365%" y2="143.962%" id="c"><stop stopColor="#65B5F0" stopOpacity="0" offset="0%"></stop><stop stopColor="#357EDD" offset="100%"></stop></linearGradient><linearGradient x1="81.342%" y1="143.962%" x2="0%" y2="143.962%" id="d"><stop stopColor="#65B5F0" stopOpacity="0" offset="0%"></stop><stop stopColor="#357EDD" offset="100%"></stop></linearGradient>
              </defs>
              <g fill="none" fillRule="evenodd">
                <path d="M50.188 16.341c.084.168.147.357.147.546 0 .651-.504 1.281-1.281 1.281-.567 0-.924-.252-1.134-.693l-2.457-5.061h-4.221v4.473c0 .714-.567 1.281-1.281 1.281a1.273 1.273 0 0 1-1.281-1.281V5.295c0-.714.567-1.281 1.281-1.281h5.397c3.486 0 4.977 1.722 4.977 4.2 0 1.638-.714 3.045-2.31 3.738l2.163 4.389zm-2.436-8.106c0-.924-.63-1.869-2.037-1.869h-4.473v3.843h4.473c1.407 0 2.037-1.029 2.037-1.974zm12.961 5.208c0 .399-.252.819-.903.819h-5.586c.126 1.092.819 1.995 2.268 1.995.798 0 1.449-.231 1.932-.609.294-.231.546-.42.924-.42.63 0 1.008.399 1.008.924 0 .588-.462.987-.903 1.26-.693.441-1.617.84-3.066.84-3.15 0-4.788-2.184-4.788-4.809 0-2.772 1.995-4.809 4.746-4.809 2.625 0 4.368 2.058 4.368 4.809zm-2.394-.966c-.189-.966-.861-1.827-1.974-1.827-1.155 0-1.953.756-2.079 1.827h4.053zm8.635-3.843c1.491 0 2.625.567 3.234 1.239.231.252.357.504.357.861 0 .567-.399.966-.987.966-.336 0-.546-.084-.777-.252-.336-.252-.903-.672-1.806-.672-1.617 0-2.457 1.26-2.457 2.667 0 1.407.84 2.667 2.457 2.667.903 0 1.47-.42 1.806-.672.231-.168.441-.252.777-.252.588 0 .987.399.987.966 0 .357-.126.609-.357.861-.609.672-1.743 1.239-3.234 1.239-3.045 0-4.956-2.121-4.956-4.809s1.911-4.809 4.956-4.809zm14.368 4.809c0 2.646-1.974 4.809-4.809 4.809s-4.809-2.163-4.809-4.809c0-2.646 1.974-4.809 4.809-4.809s4.809 2.163 4.809 4.809zm-2.478 0c0-1.407-.882-2.625-2.331-2.625-1.449 0-2.331 1.218-2.331 2.625s.882 2.625 2.331 2.625c1.449 0 2.331-1.218 2.331-2.625zm9.962-3.675c0 .63-.462 1.134-1.134 1.134-1.491 0-2.457 1.029-2.457 2.73v3.276c0 .693-.567 1.26-1.26 1.26-.693 0-1.281-.567-1.281-1.26V9.999c0-.756.525-1.281 1.281-1.281.693 0 1.26.588 1.26 1.281v.231c.441-1.008 1.239-1.596 2.457-1.596.735 0 1.134.504 1.134 1.134zm9.416-4.662v11.802c0 .693-.483 1.26-1.218 1.26s-1.218-.588-1.218-1.281v-.126c-.609.924-1.638 1.491-2.877 1.491-2.793 0-4.263-2.331-4.263-4.809s1.491-4.809 4.263-4.809c1.092 0 2.163.462 2.793 1.491V5.106c0-.693.567-1.26 1.26-1.26.693 0 1.26.567 1.26 1.26zm-7.056 8.337c0 1.47.84 2.667 2.289 2.667 1.449 0 2.247-1.26 2.247-2.667 0-1.407-.819-2.667-2.247-2.667-1.449 0-2.289 1.197-2.289 2.667zM49.075 34.824c0 .672-.546 1.176-1.218 1.176h-7.875a1.29 1.29 0 0 1-1.302-1.281V23.295a1.29 1.29 0 0 1 1.302-1.281h7.56c.672 0 1.218.504 1.218 1.176 0 .672-.546 1.197-1.218 1.197h-6.3v3.339h3.465c.651 0 1.197.525 1.197 1.197s-.546 1.176-1.197 1.176h-3.465v3.528h6.615c.672 0 1.218.525 1.218 1.197zm2.314-8.106c.315 0 .588.126.798.378l2.184 2.625 2.184-2.625c.21-.252.483-.378.798-.378.714 0 1.155.462 1.155 1.092a.992.992 0 0 1-.273.714l-2.457 2.898 2.52 2.94c.168.21.252.42.252.714 0 .609-.525 1.092-1.113 1.092-.336 0-.651-.126-.861-.378l-2.205-2.667-2.205 2.667c-.21.252-.525.378-.861.378-.588 0-1.113-.483-1.113-1.092 0-.294.084-.504.252-.714l2.52-2.94-2.457-2.898a.992.992 0 0 1-.273-.714c0-.63.441-1.092 1.155-1.092zm9.118 12.117V27.978c0-.693.483-1.26 1.218-1.26s1.218.588 1.218 1.281v.126c.609-.924 1.638-1.491 2.877-1.491 2.793 0 4.263 2.331 4.263 4.809s-1.491 4.809-4.263 4.809c-1.092 0-2.163-.462-2.793-1.491v4.074c0 .693-.567 1.26-1.26 1.26-.693 0-1.26-.567-1.26-1.26zm7.056-7.392c0-1.47-.84-2.667-2.289-2.667-1.449 0-2.247 1.26-2.247 2.667 0 1.407.819 2.667 2.247 2.667 1.449 0 2.289-1.197 2.289-2.667zm4.225.462v-3.927c0-.693.567-1.26 1.26-1.26.693 0 1.26.567 1.26 1.26v4.116c0 1.134.756 1.932 1.932 1.932s1.932-.798 1.932-1.932v-4.116c0-.693.567-1.26 1.26-1.26.693 0 1.26.567 1.26 1.26v3.927c0 2.52-1.911 4.347-4.452 4.347s-4.452-1.827-4.452-4.347zm10.534-.924c0-2.52 1.911-4.347 4.452-4.347s4.452 1.827 4.452 4.347v3.927c0 .693-.567 1.26-1.26 1.26-.693 0-1.26-.567-1.26-1.26v-4.116c0-1.134-.756-1.932-1.932-1.932s-1.932.798-1.932 1.932v4.116c0 .693-.567 1.26-1.26 1.26-.693 0-1.26-.567-1.26-1.26v-3.927zm19.585 4.452c0 3.003-1.596 4.662-5.019 4.662-1.26 0-2.478-.357-3.297-.777-.42-.21-.672-.588-.672-1.008 0-.651.441-.924 1.008-.924.399 0 .756.168 1.218.357.441.168.987.357 1.785.357 1.827 0 2.457-.819 2.457-2.52v-1.197c-.63 1.029-1.701 1.491-2.793 1.491-2.772 0-4.263-2.142-4.263-4.62s1.47-4.62 4.263-4.62c1.239 0 2.268.567 2.877 1.491v-.126c0-.714.483-1.281 1.218-1.281s1.218.567 1.218 1.26v7.455zm-7.056-4.179c0 1.407.84 2.478 2.289 2.478 1.428 0 2.247-1.155 2.247-2.478 0-1.323-.798-2.478-2.247-2.478-1.449 0-2.289 1.071-2.289 2.478zm17.68.189c0 .399-.252.819-.903.819h-5.586c.126 1.092.819 1.995 2.268 1.995.798 0 1.449-.231 1.932-.609.294-.231.546-.42.924-.42.63 0 1.008.399 1.008.924 0 .588-.462.987-.903 1.26-.693.441-1.617.84-3.066.84-3.15 0-4.788-2.184-4.788-4.809 0-2.772 1.995-4.809 4.746-4.809 2.625 0 4.368 2.058 4.368 4.809zm-2.394-.966c-.189-.966-.861-1.827-1.974-1.827-1.155 0-1.953.756-2.079 1.827h4.053z" fill="#666"></path><path fill="#FFF" d="M3 3h29v34H3z"></path><path d="M26 21.73v1.46a.756.756 0 0 1-.26.567c-.172.162-.345.243-.517.243H7.777c-.172 0-.345-.081-.518-.243A.756.756 0 0 1 7 23.189v-1.46c0-.27.086-.432.26-.486.172-.162.345-.243.517-.243h17.446c.172 0 .345.081.518.243.173.054.259.216.259.487z" fill="url(#a)"></path><path d="M26 9.73v1.46a.756.756 0 0 1-.26.567c-.172.162-.345.243-.517.243H7.777c-.172 0-.345-.081-.518-.243A.756.756 0 0 1 7 11.189V9.73c0-.27.086-.432.26-.486.172-.162.345-.243.517-.243h17.446c.172 0 .345.081.518.243.173.054.259.216.259.487z" fill="url(#b)"></path><path d="M26 27.73v1.54c0 .162-.086.325-.26.487-.172.162-.345.243-.517.243H7.777c-.172 0-.345-.081-.518-.243-.173-.162-.259-.325-.259-.487v-1.54c0-.216.086-.379.26-.487.172-.162.345-.243.517-.243h17.446c.172 0 .345.081.518.243.173.108.259.27.259.487z" fill="url(#c)"></path><path d="M26 15.73v1.54c0 .162-.086.325-.26.487-.172.162-.345.243-.517.243H7.777c-.172 0-.345-.081-.518-.243-.173-.162-.259-.325-.259-.487v-1.54c0-.216.086-.379.26-.487.172-.162.345-.243.517-.243h17.446c.172 0 .345.081.518.243.173.108.259.27.259.487z" fill="url(#d)"></path><rect stroke="#357EDD" strokeWidth="3" x="2.5" y="2.5" width="29" height="35" rx="4"></rect>
              </g>
            </svg>

          </div>
          <div className="dib mb4">
            {/* These links aren't supposed to work right now. */}
            <button className="link hover-blue f6 f5-ns dib pa3">Search</button>
            <button className="link hover-blue f6 f5-ns dib pa3">Stats</button>
            <button className="link hover-blue f6 f5-ns dib pa3">Admin</button>
            <button className="link hover-blue f6 f5-ns dib pa3">Account</button>
            <LogOut>
              <button className="link hover-blue f6 f5-ns dib pa3">Log Out</button>
            </LogOut>
          </div>
        </div>
      </nav>
    );
  }
}

export default LoggedInHeader;
