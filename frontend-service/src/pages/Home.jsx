import {useState, useEffect, useRef, useCallback, useLayoutEffect, useContext} from "react";
import { BiPlus, BiUser, BiSend, BiSolidUserCircle } from "react-icons/bi";
import { MdOutlineArrowLeft, MdOutlineArrowRight } from "react-icons/md";
import { AuthContext } from "../contexts/AuthContext";
import axios from "axios";

function Home() {
  const [text, setText] = useState("");
  //const [message, setMessage] = useState(null);
  const [chats, setChats] = useState([]);
  const [selectedChat, setSelectedChat] = useState(null);
  const [messageHistory, setMessageHistory] = useState([]);
  const [isResponseLoading, setIsResponseLoading] = useState(false);
  const [errorText, setErrorText] = useState("");
  const [isShowSidebar, setIsShowSidebar] = useState(false);
  const scrollToLastItem = useRef(null);
  const { authToken } = useContext(AuthContext);

  //console.log(authToken);
  //console.log(chats);

  const fetchChats = async () => {
    try {
      const response = await axios.get("http://localhost:8001/chats", {
        headers: { Authorization: `Bearer ${authToken}` },
      });
      setChats(response.data);
    } catch (error) {
      console.error("Error fetching chats:", error);
    }
  };

  const fetchMessages = async (chatId) => {
    try {
      const response = await axios.get(`http://localhost:8001/messages/${chatId}`, {
        headers: { Authorization: `Bearer ${authToken}` },
      });
      setMessageHistory(response.data);
    } catch (error) {
      console.error("Error fetching messages:", error);
    }
  };

  const createNewChat = async () => {
    try {
      const response = await axios.post("http://localhost:8001/create-chat", {}, {
        headers: { Authorization: `Bearer ${authToken}` },
      });
      setChats((prevChats) => [...prevChats, response.data]);
      setSelectedChat(response.data);
      setMessageHistory([]);
    } catch (error) {
      console.error("Error creating new chat:", error);
    }
  };

  const sendMessage = async (e) => {
    e.preventDefault();
    if (!text) return;

    setIsResponseLoading(true);
    setErrorText("");

    console.log(selectedChat.id, text);

    try {
      const response = await axios.post("http://localhost:8001/create-message", {
        chat_id: selectedChat.id,
        role: "user",
        content: text,
      }, {
        headers: { Authorization: `Bearer ${authToken}` },
      });
      setMessageHistory((prevMessages) => [...prevMessages, {role:"user", content:text}, response.data]);
      console.log(text, response.data);
      console.log(messageHistory)
      setText("");
      scrollToLastItem.current?.lastElementChild?.scrollIntoView({ behavior: "smooth" });
    } catch (error) {
      setErrorText(error.message);
      console.error("Error sending message:", error);
    } finally {
      setIsResponseLoading(false);
    }
  };

  const handleChatSelection = (chat) => {
    setSelectedChat(chat);
    fetchMessages(chat.id);
  };

  useEffect(() => {
    if (authToken) {
      fetchChats();
    }
  }, [authToken]);


  const toggleSidebar = useCallback(() => {
    setIsShowSidebar((prev) => !prev);
  }, []);

  useLayoutEffect(() => {
    const handleResize = () => {
      setIsShowSidebar(window.innerWidth <= 640);
    };
    handleResize();

    window.addEventListener("resize", handleResize);

    return () => {
      window.removeEventListener("resize", handleResize);
    };
  }, []);

  const uniqueTitles = Array.from(new Set(chats.map((chat) => chat.created_at).reverse()));

  return (
    <>
      <div className="container">
        <section className={`sidebar ${isShowSidebar ? "open" : ""}`}>
          <div className="sidebar-header" onClick={createNewChat} role="button">
            <BiPlus size={20} />
            <button>New Chat</button>
          </div>
          <div className="sidebar-history">
          {uniqueTitles.length > 0 && (
            <>
              <p>Ongoing</p>
              <ul>
                {uniqueTitles.map((title, idx) => (
                  <li key={idx} onClick={() => handleChatSelection(chats.find(chat => chat.created_at === title))}>
                    {title}
                  </li>
                ))}
              </ul>
            </>
          )}
          </div>
          <div className="sidebar-info">
            <div className="sidebar-info-upgrade">
              <BiUser size={20} />
              <p>Upgrade plan</p>
            </div>
            <div className="sidebar-info-user">
              <BiSolidUserCircle size={20} />
              <p>User</p>
            </div>
          </div>
        </section>

        <section className="main">
          {!selectedChat && (
            <div className="empty-chat-container">
              <img
                src="images/chatgpt-logo.svg"
                width={45}
                height={45}
                alt="ChatGPT"
              />
              <h1>Chat GPT Clone</h1>
              <h3>How can I help you today?</h3>
            </div>
          )}

          {isShowSidebar ? (
            <MdOutlineArrowRight
              className="burger"
              size={28.8}
              onClick={toggleSidebar}
            />
          ) : (
            <MdOutlineArrowLeft
              className="burger"
              size={28.8}
              onClick={toggleSidebar}
            />
          )}
          <div className="main-header">
            <ul>
              {messageHistory.map((message, idx) => (
                <li key={idx} ref={scrollToLastItem}>
                  {message.role === "user" ? (
                    <div>
                      <BiSolidUserCircle size={28.8} />
                    </div>
                  ) : (
                    <img src="images/chatgpt-logo.svg" alt="ChatGPT" />
                  )}
                  <div>
                    <p className="role-title">{message.role === "user" ? "You" : "ChatGPT"}</p>
                    <p>{message.content}</p>
                  </div>
                </li>
              ))}
            </ul>
          </div>
          <div className="main-bottom">
            {errorText && <p className="errorText">{errorText}</p>}
            <form className="form-container" onSubmit={sendMessage}>
              <input
                type="text"
                placeholder="Send a message."
                spellCheck="false"
                value={isResponseLoading ? "Processing..." : text}
                onChange={(e) => setText(e.target.value)}
                readOnly={isResponseLoading}
              />
              {!isResponseLoading && (
                <button type="submit">
                  <BiSend size={20} />
                </button>
              )}
            </form>
            <p>
              ChatGPT can make mistakes. Consider checking important
              information.
            </p>
          </div>
        </section>
      </div>
    </>
  );
}

export default Home;