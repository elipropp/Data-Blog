"""Main module for the blog"""
import streamlit as st

import src.home
import src.posts
import src.about

MAIN_PAGES = {
    "Home": src.home,
    "Posts": src.posts,
    "About": src.about,
}


def main():
    """Main function for the app"""

    st.sidebar.title('Data Viz Blog')
    st.sidebar.header('Pages')
    selection = st.sidebar.radio('Go to', list(MAIN_PAGES.keys()))

    # Every page has a main function which executes necessary code for that page
    page = MAIN_PAGES[selection]
    page.main()

    st.sidebar.header('About')
    st.sidebar.info(
        "This blog is maintained by Eli Propp. "
        "You can learn more about me on the about page or at "
        "[elipropp.github.io/Web/](https://elipropp.github.io/Web/)"
    )

    st.sidebar.header('Links')
    st.sidebar.info(
        "LinkedIn: [Eli Propp](https://www.linkedin.com/in/elipropp)  \n"
        "GitHub: [Eli Propp](https://github.com/elipropp)"
    )

if __name__ == '__main__':
    main()
