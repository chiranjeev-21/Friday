A = [1 4 8 6 1 0 0;
     4 1 2 1 0 1 0;
     2 3 1 2 0 0 1];

b = [11;
     7;
     2];

C = [4 6 3 1 0 0 0];

basic_variables = [5 6 7];

while true
    CB = C(:, basic_variables);
    Z = CB * A;
    Z_C = Z - C;
    [most_negative, l] = min(Z_C);

    if most_negative < 0
        fprintf('Entering variable %d\n', l);
    else
        disp("No negative Zj - Cj");
        disp(b);
        return;
    end
    
     ratio = b ./ A(:, l);
     i = 1;
     while i <= length(ratio)
         if ratio(i) <= 0
             ratio(i) = inf;
             i = i - 1;
         end
         i = i + 1;
     end

    [theta, k] = min(ratio);
    
    fprintf('Leaving variable %d\n\n', basic_variables(k));
    
    make_1 = A(k, l);
    A(k, :) = A(k, :) / make_1;
    b(k) = b(k) / make_1;
    
    for i = 1:size(A, 1)
        if i ~= k
            make_0 = A(i, l) / A(k, l);
            A(i, :) = A(i, :) - make_0 * A(k, :);
            b(i) = b(i) - make_0 * b(k);
        end
    end
    
    basic_variables(k) = l;
end