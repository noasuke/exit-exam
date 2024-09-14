from twitty import db
from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column

class Twitty(db.Model):
  __tablename__ = 'twitty'
  id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
  red: Mapped[int] = mapped_column(Integer, nullable=False)
  green: Mapped[int] = mapped_column(Integer, nullable=False)
  blue: Mapped[int] = mapped_column(Integer, nullable=False)
  price: Mapped[float] = mapped_column(Float, nullable=False)
  status: Mapped[str] = mapped_column(String(10), nullable=False, default='sale')

  def __repr__(self):
    return f'RGB({self.red}, {self.green}, {self.blue})'

  def get_price(self):
    red_diff = self.red-0
    green_diff = abs(self.green-170)
    blue_diff = abs(self.blue-230)

    if red_diff>=20 or green_diff>=20 or blue_diff>=20:
      return 0.0
    
    elif red_diff<20 and green_diff<20 and blue_diff<20:
      p = (red_diff+green_diff+blue_diff)*0.1
      real_price = 8.0-p

      return round(real_price, 2)