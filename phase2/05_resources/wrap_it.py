o
    n}~c�  �                   @   sV   d dl Z dd� Zdd� Zedkr'ee jd ee jd �g �ZeD ]Zee� q dS dS )	�    Nc                 C   s   | dv S )Nz5abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-� )Zletterr   r   �
wrap_it.py�check_letter   s   r   c                 C   s�  t | �|kr|�| � |�d� |�d� |S t | �|kr)|�| � |�d� |S | |d  }| | }t|�r�t|�r_| d |d � �d�}| d |� }| |d d � }|�|� t|||�S |dkrz| d |� }| |d � }|�|� t|||�S | d |d � }| |d d � �d�}|�|� t|||�S |dkr�| d |d � }| |d d � �d�}|�|� t|||�S | d |� }| |d � �d�}|�|� t|||�S )N� zEND OF FILE�   � )�len�appendr   �rindex�wrap_me�lstrip)�text�limit�outZchar_beforeZ
char_after�splitZ	next_line�restr   r   r   r      sH   









r   �__main__�   r   )	�sysr   r   �__name__�argv�int�lines�line�printr   r   r   r   �<module>   s    )
�