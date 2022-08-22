from functions.init_handlers import init_handlers
from functions.main import main
from bot import disp
from config import DB_URI

if __name__ == '__main__':
    init_handlers()
    main(disp)
